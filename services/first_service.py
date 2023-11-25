from database import MARMYTHON_DB
from typing import List
from models.first_model import UserMongoDB
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

async def read_users(skip: int = 0, limit: int = 10):
    users = []
    for user in (
        MARMYTHON_DB.test.find().skip(skip).limit(limit)
    ):
        users.append(user)
    return users