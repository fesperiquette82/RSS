from app.utils.scoring import anti_inflammatory_score, cadmium_score


def hydrate_recipe(recipe: dict) -> dict:
    cad_score, cad_label, cad_reasons = cadmium_score(recipe.get("ingredients", []))
    anti_score, anti_label, anti_reasons = anti_inflammatory_score(
        recipe.get("ingredients", []), recipe.get("techniques", [])
    )

    recipe["cadmium_profile"] = {
        "score": cad_score,
        "label": cad_label,
        "reasons": cad_reasons,
        "methodology_note": "Score heuristique de faible exposition probable au cadmium.",
    }
    recipe["anti_inflammatory_profile"] = {
        "score": anti_score,
        "label": anti_label,
        "reasons": anti_reasons,
        "methodology_note": "Score heuristique de profil anti-inflammatoire.",
    }
    recipe["id"] = str(recipe.pop("_id"))
    return recipe
