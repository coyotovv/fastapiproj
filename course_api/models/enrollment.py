from pydantic import BaseModel
from datetime import datetime

class Enrollment(BaseModel):
    student_id: str
    course_id: str
    enrollment_date: datetime = datetime.now()