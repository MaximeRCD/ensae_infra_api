from pydantic import BaseModel
from typing import List


class Ingredient(BaseModel):
    name: str
    quantity: str
    unit: str


class RecipeMongoDB(BaseModel):
    name: str
    ingredients: List[Ingredient]
