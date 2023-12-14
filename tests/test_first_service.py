import services.first_service as fs
from models.first_model import UserMongoDB, UserInMongoDB
import pytest
from  fastapi.exceptions import HTTPException

# https://pypi.org/project/pytest-asyncio/

@pytest.mark.asyncio
async def test_create_user():
    inUser =  UserInMongoDB (name='test', first_name='test', age=0)
    user_added = await fs.create_user(inUser)
    assert inUser.name == user_added['name']
    assert inUser.first_name == user_added['first_name']
    assert inUser.age == user_added['age']


@pytest.mark.asyncio
async def test_read_user():
    searched_user =  UserInMongoDB (name='test', first_name='test', age=0)
    research = await fs.read_user(searched_user.name)
    assert searched_user.name == research['name']
    assert searched_user.first_name == research['first_name']
    assert searched_user.age == research['age']

@pytest.mark.asyncio
async def test_put_user():
    modified_user =  UserInMongoDB (name='test', first_name='another_test', age=0)
    put_user = await fs.update_user(user_name=modified_user.name, user=modified_user)
    assert modified_user.name == put_user['name']
    assert modified_user.first_name == put_user['first_name']
    assert modified_user.age == put_user['age']

@pytest.mark.asyncio
async def test_delete_user():
    user_to_del =  UserInMongoDB (name='test', first_name='another_test', age=0)
    unknown_user_to_del =  UserInMongoDB (name='unknown', first_name='unknown', age=0)

    deleted_user = await fs.delete_user(user_name=user_to_del.name)

    assert user_to_del.name == deleted_user['name']
    assert user_to_del.first_name == deleted_user['first_name']
    assert user_to_del.age == deleted_user['age']

    try :
        await fs.delete_user(user_name=unknown_user_to_del.name)
    except Exception as e:
        assert type(e) == HTTPException
        assert e.detail == "user not found"
        assert e.status_code == 404


@pytest.mark.asyncio
async def test_sum_ages():
    users = await fs.read_users()
    result = fs.sum_ages(users)
    assert  result >= 0
    assert type(result) == int 