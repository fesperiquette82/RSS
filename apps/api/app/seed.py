import json
from pathlib import Path

from app.db.mongo import MongoDB


def run_seed() -> None:
    MongoDB.connect()
    db = MongoDB.get_db()
    seed_path = Path("/seeds/recipes.json")
    if not seed_path.exists():
        seed_path = Path(__file__).resolve().parents[3] / "seeds" / "recipes.json"
    recipes = json.loads(seed_path.read_text(encoding="utf-8"))

    db.recipes.delete_many({})
    if recipes:
        db.recipes.insert_many(recipes)

    db.app_state.update_one({"_id": "favorites"}, {"$setOnInsert": {"recipe_ids": []}}, upsert=True)
    db.app_state.update_one({"_id": "shopping_list"}, {"$setOnInsert": {"items": []}}, upsert=True)
    db.app_state.update_one(
        {"_id": "preferences"},
        {"$setOnInsert": {"language": "fr", "show_methodology_on_start": True}},
        upsert=True,
    )
    print(f"Seed loaded with {len(recipes)} recipes")
    MongoDB.disconnect()


if __name__ == "__main__":
    run_seed()
