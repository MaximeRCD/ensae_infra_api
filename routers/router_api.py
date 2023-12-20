# %%
import sys

sys.path.append("/home/syrine/Documents/ensae/projet infra/ensae_infra_api/")
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from models.model_recipe import RecipeMongoDB, RecipeInMongoDB, Ingredient
from services.service_api import get_shopping_list

from services import service_DB
from fastapi import HTTPException

# %%

router_api = APIRouter(prefix="/recipe", tags=["Recipe"])


@router_api.post("/get_shopping_list", response_model=List[Ingredient])
async def _get_shopping_list(recipe: List[str], nb_pers: int):
    return await get_shopping_list(strings=recipe, nb_pers=nb_pers)


router_database = APIRouter(prefix="/database", tags=["Database"])


@router_database.post("/create_database_recipe", response_model=RecipeMongoDB)
async def create_recipe(recipe: RecipeInMongoDB):
    return await service_DB.create_recipe(recipe=recipe)


@router_database.get("/read_all_recipes", response_model=List[RecipeMongoDB])
async def read_all_recipes(skip: int = 0, limit: int = 10):
    return await service_DB.read_recipes(skip=skip, limit=limit)


@router_database.get("/read_recipe/{recipe_name}", response_model=RecipeMongoDB)
async def read_single_recipe(recipe_name: str):
    return await service_DB.read_recipe(recipe_name)


@router_database.put("/update_recipe/{recipe_name}", response_model=RecipeMongoDB)
async def update_single_recipe(recipe_name: str, recipe: RecipeInMongoDB):
    try:
        return await service_DB.update_recipe(recipe_name, recipe)
    except HTTPException as e:
        return e


@router_database.delete("/delete_recipe/{recipe_name}", response_model=RecipeMongoDB)
async def delete_single_recipe(recipe_name: str):
    try:
        return await service_DB.delete_recipe(recipe_name)
    except HTTPException as e:
        return e
