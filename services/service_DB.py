from database import MARMYTHON_DB
from typing import List
from models.recipe_model import RecipeMongoDB
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from bson import ObjectId


async def read_recipes(skip: int = 0, limit: int = 10):
    recipes = []
    for recipe in MARMYTHON_DB.recipes.find().skip(skip).limit(limit):
        recipes.append(recipe)
    return recipes


async def create_recipe(recipe: RecipeMongoDB):
    recipe_dict = recipe.dict()
    try:
        result = MARMYTHON_DB.recipes.insert_one(recipe_dict)
        recipe_dict["_id"] = ObjectId(result.inserted_id)
        return recipe_dict
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="A recipe with the same name already exists",
        )


async def read_recipe(recipe_name: str):
    recipe = MARMYTHON_DB.recipes.find_one({"name": recipe_name})
    if recipe:
        return recipe
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")


async def update_recipe(recipe_name: str, recipe: RecipeMongoDB):
    updated_recipe = MARMYTHON_DB.recipes.find_one_and_update(
        {"name": recipe_name}, {"$set": recipe.dict()}, return_document=True
    )
    if updated_recipe:
        return updated_recipe
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")


async def delete_recipe(recipe_name: str):
    deleted_recipe = MARMYTHON_DB.recipes.find_one_and_delete({"name": recipe_name})
    if deleted_recipe:
        return deleted_recipe
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")