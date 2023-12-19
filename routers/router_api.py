from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from services import service_scraping,service_api,service_DB
from models.model_recipe import RecipeMongoDB, RecipeInMongoDB, Ingredient


router_api = APIRouter(prefix="/recipe", tags=["Recipe"])


"""@router_api.post("/", response_model=RecipeMongoDB)
async def create_recipe(recipe: RecipeInMongoDB):
    return await service_DB.create_recipe(recipe=recipe)"""

@router_api.post("/", response_model=List[Ingredient]) 
async def _get_shopping_list(recipe: List[str],nb_pers:int):
    return await service_api._get_shopping_list(recipe=recipe,nb_pers=nb_pers)

    

  
 


