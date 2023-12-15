from database import MARMYTHON_DB
from typing import List
from models.first_model import UserMongoDB, UserInMongoDB
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from bson import ObjectId


async def read_users(skip: int = 0, limit: int = 10):
    users = []
    for user in MARMYTHON_DB.test.find().skip(skip).limit(limit):
        users.append(user)
    return users


async def create_user(user: UserInMongoDB):
    user_dict = user.dict()
    try:
        result = MARMYTHON_DB.test.insert_one(user_dict)
        user_dict["_id"] = ObjectId(result.inserted_id)
        return user_dict
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="A user with the same name and telephone number already exists",
        )


async def read_user(user_name: str):
    user = MARMYTHON_DB.test.find_one({"name": user_name})
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="user not found")


async def update_user(user_name: str, user: UserInMongoDB):
    updated_user = MARMYTHON_DB.test.find_one_and_update(
        {"name": user_name}, {"$set": user.dict()}, return_document=True
    )
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="user not found")


async def delete_user(user_name: str):
    deleted_user = MARMYTHON_DB.test.find_one_and_delete({"name": user_name})
    if deleted_user:
        return deleted_user
    else:
        raise HTTPException(status_code=404, detail="user not found")
