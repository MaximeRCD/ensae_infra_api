from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from services import service_scraping,service_api,service_DB
from models.model_recipe import RecipeMongoDB, RecipeInMongoDB


router_api = APIRouter(prefix="/recipe", tags=["user"])


"""@router_api.post("/", response_model=RecipeMongoDB)
async def create_recipe(recipe: RecipeInMongoDB):
    return await service_DB.create_recipe(recipe=recipe)"""

@router_api.post("/", response_model=List[Ingredient]) #add ingredient object inside list
async def _get_shopping_list(recipe: List[str],nb_pers:int):
    return await service_api._get_shopping_list(recipe=recipe,nb_pers=nb_pers)

    ## doit on créer une classe pour les shopping lists ?
    

@first_router.put("/{user_name}", response_model=UserMongoDB)
async def update_user(user_name: str, user: UserInMongoDB):
    return await first_service.update_user(user_name=user_name, user=user)

  
 


