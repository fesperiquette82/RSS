from app.utils.scoring import anti_inflammatory_score, cadmium_score


def test_cadmium_score_penalty():
    score, label, _ = cadmium_score(["chocolat noir", "riz", "poulet"])
    assert score < 90
    assert label in {"faible", "modérée", "attention plus élevée", "très faible"}


def test_anti_inflammatory_bonus():
    score, label, _ = anti_inflammatory_score(
        ["huile d'olive", "courgette", "ail", "cabillaud"], ["four"]
    )
    assert score >= 65
    assert label in {"bon", "très bon"}
