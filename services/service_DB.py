import pymongo
from database import MARMYTHON_DB
from models.model_recipe import RecipeMongoDB, RecipeInMongoDB



def is_string_in_DB(string):
    return MARMYTHON_DB.recipes.find_one({"name":string}) is not None

def get_recipe_from_DB(string):
    return MARMYTHON_DB.recipes.find_one({"name":string})

def get_recipe_from_DB_by_id(id):
    return MARMYTHON_DB.recipes.find_one({"_id":id})

def get_recipe_from_DB_by_url(url):
    return MARMYTHON_DB.recipes.find_one({"url":url})

async def create_recipe(recipe : RecipeInMongoDB):
    recipe_dict = recipe.dict()
    try:
        result = MARMYTHON_DB.recipe.insert_one(recipe_dict)
        recipe_dict["_id"] = ObjectId(result.inserted_id)
        return recipe_dict
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="A user with the same name and telephone number already exists",
        )