from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Course(BaseModel):
    title: str
    description: Optional[str] = None
    instructor_id: str
    creation_date: datetime = datetime.now()