from pydantic import BaseModel, Field
from typing import Optional

# Pydantic model for Instructor entity
class Instructor(BaseModel):
    name: str
    email: str = Field(..., example="jane.doe@example.com")
    bio: Optional[str] = None