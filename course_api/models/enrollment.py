from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId
from datetime import datetime
from .instructor import PyObjectId 

class Enrollment(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    student_id: str
    course_id: str
    enrollment_date: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        json_encoders = {ObjectId: str}
        populate_by_name = True