from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId

from .instructor import PyObjectId 

class Student(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    email: EmailStr
    student_id: str
    
    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True