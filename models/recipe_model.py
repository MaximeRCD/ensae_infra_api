from pydantic import BaseModel
from typing import List


class RecipeMongoDB(BaseModel):
    name: str
    ingredients: List[str]
    quantities: List[str]
