from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str
    email: str
    bio: Optional[str] = None