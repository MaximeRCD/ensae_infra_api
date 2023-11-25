from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from services import first_service
from models.first_model import UserMongoDB


first_router = APIRouter(prefix="/user", tags=["user"])


@first_router.get("/", tags=["user"], response_model=List[UserMongoDB])
async def get_users():
    return await first_service.read_users()