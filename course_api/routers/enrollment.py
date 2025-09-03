# file: routers/enrollment.py
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.enrollment import Enrollment
from models.course import Course
from crud.enrollment import (
    create_enrollment,
    get_all_enrollments,
    delete_enrollment,
    get_students_by_course,
    get_courses_by_student
)

router = APIRouter()

@router.post("/", response_model=str, tags=["Enrollments"])
def enroll_student(enrollment: Enrollment):
    return create_enrollment(enrollment)

@router.get("/", response_model=List[Enrollment], tags=["Enrollments"])
def list_all_enrollments():
    return get_all_enrollments()

@router.delete("/{id}", response_model=bool, tags=["Enrollments"])
def remove_enrollment(id: str):
    was_deleted = delete_enrollment(id)
    if not was_deleted:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return was_deleted

@router.get("/students/{course_id}/courses", response_model=List[Enrollment], tags=["Enrollments"])
def get_students_for_course(course_id: str):
    return get_students_by_course(course_id)

@router.get("/courses/{student_id}/courses", response_model=List[Enrollment], tags=["Enrollments"])
def get_courses_for_student(student_id: str):
    return get_courses_by_student(student_id)