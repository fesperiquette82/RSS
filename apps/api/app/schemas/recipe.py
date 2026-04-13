from pydantic import BaseModel, Field


class RecipeBase(BaseModel):
    title: str
    description: str
    category: str
    difficulty: str
    duration_minutes: int
    servings: int
    budget_level: str
    ingredients: list[str]
    steps: list[str]
    tags: list[str] = Field(default_factory=list)
    techniques: list[str] = Field(default_factory=list)


class ScoreExplanation(BaseModel):
    score: int
    label: str
    reasons: list[str]
    methodology_note: str


class RecipeOut(RecipeBase):
    id: str
    cadmium_profile: ScoreExplanation
    anti_inflammatory_profile: ScoreExplanation


class RecipeListOut(BaseModel):
    items: list[RecipeOut]
    total: int


class SearchByIngredientsIn(BaseModel):
    ingredients: list[str]
    match_all: bool = False
