from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from services import first_service
from models.first_model import UserMongoDB, UserInMongoDB


first_router = APIRouter(prefix="/user", tags=["user"])


@first_router.get("/", tags=["user"], response_model=List[UserMongoDB])
async def get_users():
    return await first_service.read_users()


@first_router.post("/", response_model=UserMongoDB)
async def create_user(user: UserInMongoDB):
    return await first_service.create_user(user=user)


@first_router.get("/{user_name}", response_model=UserMongoDB)
async def read_user(user_name: str):
    return await first_service.read_user(user_name=user_name)


@first_router.put("/{user_name}", response_model=UserMongoDB)
async def update_user(user_name: str, user: UserInMongoDB):
    return await first_service.update_user(user_name=user_name, user=user)


@first_router.delete("/{user_name}", response_model=UserMongoDB)
async def delete_user(user_name: str):
    return await first_service.delete_user(user_name=user_name)
