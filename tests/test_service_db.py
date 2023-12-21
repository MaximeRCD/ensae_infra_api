import services.service_DB as s_db
from models.model_recipe import RecipeInMongoDB, RecipeMongoDB, Ingredient
import pytest
from  fastapi.exceptions import HTTPException

# https://pypi.org/project/pytest-asyncio/

@pytest.mark.asyncio
async def test_create_recipe_from_string():
    input_recipe =  {'name': 'test_string', 'ingredients': [{'name': 'string', 'quantity': '0.0', 'unit': 'string'}], 'url': 'string', 'nb_persons': 4}
    recipe_added = await s_db.create_recipe(input_recipe)
    assert input_recipe['name'] == recipe_added['name']
    assert input_recipe['ingredients'] == recipe_added['ingredients']
    assert input_recipe['nb_persons'] == recipe_added['nb_persons']

@pytest.mark.asyncio
async def test_delete_recipe():
    recipe_to_del =  RecipeMongoDB (name="test_string", ingredients=[Ingredient(name='string', quantity= 0.0, unit='string')], url='string', nb_persons=4)
    unknown_recipe_to_del =  RecipeMongoDB (name="unknown", ingredients=[Ingredient(name='string', quantity= 0.0, unit='string')], url='string', nb_persons=4)
    deleted_recipe = await s_db.delete_recipe(recipe_name=recipe_to_del.name)

    assert recipe_to_del.name == deleted_recipe['name']
    assert recipe_to_del.url == deleted_recipe['url']
    assert recipe_to_del.nb_persons == deleted_recipe['nb_persons']

    try :
        await s_db.delete_recipe(recipe_name=unknown_recipe_to_del.name)
    except Exception as e:
        assert type(e) == HTTPException
        assert e.detail == "Recipe not found"
        assert e.status_code == 404

@pytest.mark.asyncio
async def test_create_recipe_no_zero_person():
    input_recipe =  {'name': 'test_string', 'ingredients': [{'name': 'string', 'quantity': '0.0', 'unit': 'string'}], 'url': 'string', 'nb_persons': 0}
    recipe_added = await s_db.create_recipe(input_recipe)
    assert input_recipe['name'] == recipe_added['name']
    assert recipe_added['nb_persons'] == 1
    await s_db.delete_recipe(recipe_name=input_recipe['name'])

@pytest.mark.asyncio
async def test_read_recipe():
    recipe_to_read =  RecipeMongoDB(name="test_string", ingredients=[Ingredient(name='string', quantity= 0.0, unit='string')], url='string', nb_persons=4)
    _ = await s_db.create_recipe(recipe_to_read)
    read_recipe = await s_db.read_recipe(recipe_name=recipe_to_read.name)
    assert recipe_to_read.name == read_recipe['name']
    assert recipe_to_read.url == read_recipe['url']
    assert recipe_to_read.nb_persons == read_recipe['nb_persons']
    await s_db.delete_recipe(recipe_name=read_recipe['name'])


@pytest.mark.asyncio
async def test_put_user():
    first_recipe =  RecipeMongoDB(name="test_string", ingredients=[Ingredient(name='string', quantity= 0.0, unit='string')], url='string', nb_persons=4)
    _ = await s_db.create_recipe(first_recipe)
    recipe_to_put =  RecipeMongoDB(name="changed_string", ingredients=[Ingredient(name='string', quantity= 0.0, unit='string')], url='string', nb_persons=4)
    updated_recipe = await s_db.update_recipe(recipe_name=first_recipe.name, recipe=recipe_to_put)
    assert recipe_to_put.name == updated_recipe['name']
    try :
        await s_db.delete_recipe(recipe_name=first_recipe.name)
    except Exception as e:
        assert type(e) == HTTPException
        assert e.detail == "Recipe not found"
        assert e.status_code == 404
