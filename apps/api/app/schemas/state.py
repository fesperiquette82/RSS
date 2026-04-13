from pydantic import BaseModel, Field


class FavoriteOut(BaseModel):
    recipe_ids: list[str]


class ShoppingListOut(BaseModel):
    items: list[str]


class ShoppingListIn(BaseModel):
    item: str = Field(min_length=1)


class Preferences(BaseModel):
    language: str = "fr"
    show_methodology_on_start: bool = True
