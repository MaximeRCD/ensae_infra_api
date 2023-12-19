#%%
import sys
sys.path.append('/home/syrine/Documents/ensae/projet infra/ensae_infra_api/')
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from models.model_recipe import RecipeMongoDB, RecipeInMongoDB, Ingredient
from services.service_api import get_shopping_list
#%%

router_api = APIRouter(prefix="/recipe", tags=["Recipe"])


"""@router_api.post("/", response_model=RecipeMongoDB)
async def create_recipe(recipe: RecipeInMongoDB):
    return await service_DB.create_recipe(recipe=recipe)"""

@router_api.post("/", response_model=List[Ingredient]) 
async def _get_shopping_list(recipe: List[str],nb_pers:int):
    return await get_shopping_list(recipe=recipe,nb_pers=nb_pers)

    
