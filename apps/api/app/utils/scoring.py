from typing import Iterable


def _contains_any(texts: Iterable[str], keywords: list[str]) -> bool:
    blob = " ".join(t.lower() for t in texts)
    return any(k in blob for k in keywords)


def cadmium_score(ingredients: list[str]) -> tuple[int, str, list[str]]:
    score = 100
    reasons: list[str] = []

    strong = {
        "abats": ["foie", "rognon", "abats"],
        "coquillages/crustacés": ["moule", "huître", "crevette", "crabe", "coquillage"],
        "cacao/chocolat": ["cacao", "chocolat"],
        "algues": ["algue", "spiruline", "nori"],
        "noix/graines": ["amande", "noix", "graines", "sésame", "cacahuète"],
        "champignons": ["champignon"],
    }
    moderate = {
        "céréales complètes": ["complet", "son", "germe"],
        "quinoa": ["quinoa"],
        "avoine": ["avoine", "flocons d'avoine"],
        "riz": ["riz"],
        "pommes de terre": ["pomme de terre"],
        "légumineuses": ["lentille", "pois chiche", "haricot"],
    }
    bonuses = {
        "oeufs": ["oeuf", "œuf"],
        "laitages nature": ["yaourt", "skyr", "fromage blanc", "lait"],
        "volaille": ["poulet", "dinde"],
        "légumes-fruits": ["courgette", "tomate", "poivron", "aubergine"],
        "fruits frais": ["pomme", "poire", "banane", "fruit"],
    }

    for family, keys in strong.items():
        if _contains_any(ingredients, keys):
            score -= 20
            reasons.append(f"Présence potentielle de {family} (pénalité forte).")

    for family, keys in moderate.items():
        if _contains_any(ingredients, keys):
            score -= 8
            reasons.append(f"Présence de {family} (pénalité modérée).")

    for family, keys in bonuses.items():
        if _contains_any(ingredients, keys):
            score += 4
            reasons.append(f"Présence de {family} (bonus léger).")

    score = max(0, min(100, score))

    if score >= 85:
        label = "très faible"
    elif score >= 70:
        label = "faible"
    elif score >= 50:
        label = "modérée"
    else:
        label = "attention plus élevée"

    return score, label, reasons


def anti_inflammatory_score(
    ingredients: list[str], techniques: list[str]
) -> tuple[int, str, list[str]]:
    score = 50
    reasons: list[str] = []

    bonuses = {
        "huile d'olive": ["huile d'olive"],
        "légumes variés": [
            "courgette",
            "carotte",
            "tomate",
            "poivron",
            "épinard",
            "brocoli",
        ],
        "fruits frais": ["pomme", "poire", "banane", "fruit"],
        "ail/oignon/herbes/citron": ["ail", "oignon", "persil", "herbes", "citron"],
        "poisson simple": ["cabillaud", "colin", "sardine", "thon", "poisson"],
    }
    maluses = {
        "ultra-transformé": ["nuggets", "charcuterie industrielle", "snack industriel"],
        "sucre élevé": ["sirop", "sucre", "bonbon"],
        "sauces industrielles": ["sauce industrielle", "ketchup", "barbecue"],
    }

    for family, keys in bonuses.items():
        if _contains_any(ingredients, keys):
            score += 7
            reasons.append(f"Atout: {family}.")

    for family, keys in maluses.items():
        if _contains_any(ingredients, keys):
            score -= 10
            reasons.append(f"Point de vigilance: {family}.")

    if _contains_any(techniques, ["friture", "frire"]):
        score -= 10
        reasons.append("Point de vigilance: friture.")

    if _contains_any(techniques, ["vapeur", "mijoté", "four", "poêle simple"]):
        score += 5
        reasons.append("Préparation peu transformée.")

    score = max(0, min(100, score))

    if score >= 80:
        label = "très bon"
    elif score >= 65:
        label = "bon"
    elif score >= 50:
        label = "neutre"
    else:
        label = "moins favorable"

    return score, label, reasons
