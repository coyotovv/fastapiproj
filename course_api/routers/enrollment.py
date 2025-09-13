from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from database import db
from models.enrollment import Enrollment
from datetime import datetime
from pymongo import ReturnDocument

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

class EnrollmentOut(BaseModel):
    id: str
    student_id: str
    course_id: str
    enrollment_date: datetime

@router.post("/", response_model=EnrollmentOut, status_code=status.HTTP_201_CREATED)
def create_enrollment(enrollment: Enrollment):
    # First, check if the student_id and course_id exist in their respective collections
    student_exists = db.students.find_one({"_id": ObjectId(enrollment.student_id)})
    course_exists = db.courses.find_one({"_id": ObjectId(enrollment.course_id)})

    if not student_exists:
        raise HTTPException(status_code=404, detail=f"Student with ID '{enrollment.student_id}' not found.")
    if not course_exists:
        raise HTTPException(status_code=404, detail=f"Course with ID '{enrollment.course_id}' not found.")

    # If both exist, proceed with the enrollment
    enrollment_dict = enrollment.dict()
    result = db.enrollments.insert_one(enrollment_dict)
    enrollment_dict["id"] = str(result.inserted_id)

    return enrollment_dict


# DELETE endpoint to remove an enrollment
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_enrollment(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid enrollment ID format")

    result = db.enrollments.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    return None

# GET endpoint to list a student's courses
@router.get("/students/{id}/courses/")
def get_student_courses(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format")

    # Find all enrollment documents for the given student
    enrollments = db.enrollments.find({"student_id": id})
    
    # Get the course_ids from the enrollment documents
    course_ids = [enrollment["course_id"] for enrollment in enrollments]

    # Find the actual course documents using the list of IDs
    courses = list(db.courses.find({"_id": {"$in": [ObjectId(cid) for cid in course_ids]}}))

    for course in courses:
        course["id"] = str(course["_id"])
        course.pop("_id")
    
    return courses

# GET endpoint to list a course's students
@router.get("/courses/{id}/students/")
def get_course_students(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid course ID format")

    # Find all enrollment documents for the given course
    enrollments = db.enrollments.find({"course_id": id})
    
    # Get the student_ids from the enrollment documents
    student_ids = [enrollment["student_id"] for enrollment in enrollments]

    # Find the actual student documents using the list of IDs
    students = list(db.students.find({"_id": {"$in": [ObjectId(sid) for sid in student_ids]}}))

    for student in students:
        student["id"] = str(student["_id"])
        student.pop("_id")
    
    return students
