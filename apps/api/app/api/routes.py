from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.deps import get_db
from app.schemas.recipe import RecipeListOut, RecipeOut, SearchByIngredientsIn
from app.schemas.state import FavoriteOut, Preferences, ShoppingListIn, ShoppingListOut
from app.services.recipe_service import hydrate_recipe

router = APIRouter()


@router.get("/recipes", response_model=RecipeListOut)
def list_recipes(
    category: str | None = None,
    q: str | None = None,
    max_duration: int | None = None,
    min_cadmium_score: int | None = Query(default=None, ge=0, le=100),
    db=Depends(get_db),
):
    query: dict = {}
    if category:
        query["category"] = category
    docs = list(db.recipes.find(query))
    hydrated = [hydrate_recipe(d) for d in docs]

    if q:
        q_lower = q.lower()
        hydrated = [
            r
            for r in hydrated
            if q_lower in r["title"].lower()
            or any(q_lower in i.lower() for i in r["ingredients"])
        ]
    if max_duration is not None:
        hydrated = [r for r in hydrated if r["duration_minutes"] <= max_duration]
    if min_cadmium_score is not None:
        hydrated = [
            r for r in hydrated if r["cadmium_profile"]["score"] >= min_cadmium_score
        ]

    return {"items": hydrated, "total": len(hydrated)}


@router.get("/recipes/{recipe_id}", response_model=RecipeOut)
def get_recipe(recipe_id: str, db=Depends(get_db)):
    from bson import ObjectId

    doc = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not doc:
        raise HTTPException(status_code=404, detail="Recette introuvable")
    return hydrate_recipe(doc)


@router.post("/recipes/search-by-ingredients", response_model=RecipeListOut)
def search_by_ingredients(payload: SearchByIngredientsIn, db=Depends(get_db)):
    docs = list(db.recipes.find())
    user_ings = {i.strip().lower() for i in payload.ingredients}

    hydrated = []
    for doc in docs:
        recipe_ings = {i.lower() for i in doc.get("ingredients", [])}
        if payload.match_all:
            ok = recipe_ings.issubset(user_ings)
        else:
            ok = len(recipe_ings.intersection(user_ings)) >= 2
        if ok:
            hydrated.append(hydrate_recipe(doc))

    return {"items": hydrated, "total": len(hydrated)}


@router.get("/ingredients/search")
def ingredient_search(q: str, db=Depends(get_db)):
    docs = list(db.recipes.find())
    all_ingredients: set[str] = set()
    for d in docs:
        all_ingredients.update(d.get("ingredients", []))
    ql = q.lower().strip()
    return sorted([i for i in all_ingredients if ql in i.lower()])[:20]


@router.get("/favorites", response_model=FavoriteOut)
def get_favorites(db=Depends(get_db)):
    state = db.app_state.find_one({"_id": "favorites"}) or {"recipe_ids": []}
    return {"recipe_ids": state.get("recipe_ids", [])}


@router.post("/favorites/{recipe_id}", response_model=FavoriteOut)
def add_favorite(recipe_id: str, db=Depends(get_db)):
    db.app_state.update_one(
        {"_id": "favorites"},
        {"$addToSet": {"recipe_ids": recipe_id}},
        upsert=True,
    )
    return get_favorites(db)


@router.delete("/favorites/{recipe_id}", response_model=FavoriteOut)
def remove_favorite(recipe_id: str, db=Depends(get_db)):
    db.app_state.update_one(
        {"_id": "favorites"},
        {"$pull": {"recipe_ids": recipe_id}},
        upsert=True,
    )
    return get_favorites(db)


@router.get("/shopping-list", response_model=ShoppingListOut)
def get_shopping_list(db=Depends(get_db)):
    state = db.app_state.find_one({"_id": "shopping_list"}) or {"items": []}
    return {"items": state.get("items", [])}


@router.post("/shopping-list/items", response_model=ShoppingListOut)
def add_shopping_item(payload: ShoppingListIn, db=Depends(get_db)):
    db.app_state.update_one(
        {"_id": "shopping_list"},
        {"$addToSet": {"items": payload.item.strip()}},
        upsert=True,
    )
    return get_shopping_list(db)


@router.delete("/shopping-list/items/{name}", response_model=ShoppingListOut)
def remove_shopping_item(name: str, db=Depends(get_db)):
    db.app_state.update_one(
        {"_id": "shopping_list"},
        {"$pull": {"items": name}},
        upsert=True,
    )
    return get_shopping_list(db)


@router.get("/preferences", response_model=Preferences)
def get_preferences(db=Depends(get_db)):
    state = db.app_state.find_one({"_id": "preferences"}) or {}
    return {
        "language": state.get("language", "fr"),
        "show_methodology_on_start": state.get("show_methodology_on_start", True),
    }


@router.put("/preferences", response_model=Preferences)
def update_preferences(payload: Preferences, db=Depends(get_db)):
    db.app_state.update_one(
        {"_id": "preferences"},
        {"$set": payload.model_dump()},
        upsert=True,
    )
    return payload
