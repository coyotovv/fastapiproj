from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from database import db
from models.enrollment import Enrollment
from datetime import datetime
from pymongo import ReturnDocument
from typing import List

class BulkEnrollment(BaseModel):
    student_ids: List[str]
    course_id: str

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
    student_exists = db.students.find_one({"_id": ObjectId(enrollment.student_id)})
    course_exists = db.courses.find_one({"_id": ObjectId(enrollment.course_id)})

    if not student_exists:
        raise HTTPException(status_code=404, detail=f"Student with ID '{enrollment.student_id}' not found.")
    if not course_exists:
        raise HTTPException(status_code=404, detail=f"Course with ID '{enrollment.course_id}' not found.")

    enrollment_dict = enrollment.dict()
    result = db.enrollments.insert_one(enrollment_dict)
    enrollment_dict["id"] = str(result.inserted_id)
    
    return enrollment_dict



@router.post("/bulk/", status_code=status.HTTP_201_CREATED)
def bulk_enroll_students(bulk_enrollment: BulkEnrollment):
    # Check if the course exists
    course_exists = db.courses.find_one({"_id": ObjectId(bulk_enrollment.course_id)})
    if not course_exists:
        raise HTTPException(status_code=404, detail=f"Course with ID '{bulk_enrollment.course_id}' not found.")

    # Check if all students exist and get their IDs
    valid_student_ids = []
    for student_id in bulk_enrollment.student_ids:
        if not ObjectId.is_valid(student_id):
            raise HTTPException(status_code=400, detail=f"Invalid student ID '{student_id}' format.")
        if not db.students.find_one({"_id": ObjectId(student_id)}):
            raise HTTPException(status_code=404, detail=f"Student with ID '{student_id}' not found.")
        valid_student_ids.append(student_id)

    # Create enrollment documents for each student
    enrollments_to_insert = []
    for student_id in valid_student_ids:
        enrollments_to_insert.append({
            "student_id": student_id,
            "course_id": bulk_enrollment.course_id,
            "enrollment_date": datetime.now()
        })

    # Insert all documents in one go for efficiency
    if enrollments_to_insert:
        db.enrollments.insert_many(enrollments_to_insert)

    return {"message": f"Successfully enrolled {len(enrollments_to_insert)} students."}



@router.get("/")
def list_enrollments():
    enrollments = list(db.enrollments.find({}))
    for enrollment in enrollments:
        enrollment["id"] = str(enrollment["_id"])
        enrollment.pop("_id")
    return enrollments

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_enrollment(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid enrollment ID format")

    result = db.enrollments.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    return None

@router.get("/students/{id}/courses/")
def get_student_courses(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format")

    enrollments = db.enrollments.find({"student_id": id})
    course_ids = [enrollment["course_id"] for enrollment in enrollments]

    courses = list(db.courses.find({"_id": {"$in": [ObjectId(cid) for cid in course_ids]}}))

    for course in courses:
        course["id"] = str(course["_id"])
        course.pop("_id")
    
    return courses

@router.get("/courses/{id}/students/")
def get_course_students(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid course ID format")

    enrollments = db.enrollments.find({"course_id": id})
    student_ids = [enrollment["student_id"] for enrollment in enrollments]

    students = list(db.students.find({"_id": {"$in": [ObjectId(sid) for sid in student_ids]}}))

    for student in students:
        student["id"] = str(student["_id"])
        student.pop("_id")
    
    return students