# file: models/instructor.py
from pydantic import BaseModel, Field, EmailStr
from typing import Any, Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: Any) -> None:
        field_schema.update(type='string')

# Now your Instructor model and other models that import PyObjectId will work correctly.
class Instructor(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    email: EmailStr
    bio: Optional[str] = None
    
    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True