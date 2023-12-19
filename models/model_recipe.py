from pydantic import BaseModel
from bson import ObjectId
from typing import Optional, List, Tuple

class RecipeMongoDB(BaseModel):
    _id: ObjectId  # Use PyMongo's ObjectId type
    name: str
    ingredients: List[List[str]]  #va devenir List[ingrédient]
    url: str
    nb_persons: int

class RecipeInMongoDB(BaseModel):
    name: str
    ingredients: List[List[str]]
    url: str
    nb_persons: int

    # On ne sait pas bien comment créer une instance de classe 
    
#add un type ingrédient (qui a comme instances un nom et une quantité et une unit)
    