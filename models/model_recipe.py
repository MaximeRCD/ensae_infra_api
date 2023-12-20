from pydantic import BaseModel
from bson import ObjectId
from typing import Optional, List, Tuple

class Ingredient(BaseModel):
    name: str
    quantity: float
    unit: str

class RecipeInMongoDB(BaseModel):
    _id: ObjectId  
    name: str
    ingredients: List[Ingredient]  
    url: str
    nb_persons: int

class RecipeMongoDB(BaseModel):
    name: str
    ingredients: List[Ingredient]
    url: str
    nb_persons: int
    

    