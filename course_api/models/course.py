from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId
from .instructor import PyObjectId 

class Course(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    instructor_id: str
    
    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True