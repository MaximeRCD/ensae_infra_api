from pydantic import BaseModel
from bson import ObjectId

class UserMongoDB(BaseModel):
    _id: ObjectId  # Use PyMongo's ObjectId type
    name: str
    first_name: str
    age: int

class UserInMongoDB(BaseModel): #
    name: str
    first_name: str
    age: int
