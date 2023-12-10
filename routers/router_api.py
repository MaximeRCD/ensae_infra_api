from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from services import service_scraping,service_api,service_DB
from models.model_recipe import RecipeMongoDB, RecipeInMongoDB


router_api = APIRouter(prefix="/user", tags=["user"])


@router_api.post("/", response_model=RecipeMongoDB)
async def create_recipe(recipe: RecipeInMongoDB):
    return await service_DB.create_recipe(recipe=recipe)

@router_api.post("/")
async def _get_shopping_list(string):
    return service_api._get_shopping_list(string)

    ## doit on créer une classe pour les shopping lists ?

  
 


