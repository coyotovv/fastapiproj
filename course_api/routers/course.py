# file: routers/course.py
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.course import Course
from crud.course import (
    create_course,
    get_all_courses,
    get_course_by_id,
    get_courses_by_instructor_id,
    update_course,
    delete_course
)

router = APIRouter()

@router.post("/", response_model=str, tags=["Courses"])
def create_new_course(course: Course):
    return create_course(course)

@router.get("/", response_model=List[Course], tags=["Courses"])
def list_courses():
    return get_all_courses()

@router.get("/{id}", response_model=Course, tags=["Courses"])
def get_course(id: str):
    course = get_course_by_id(id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/by-instructor/{instructor_id}", response_model=List[Course], tags=["Courses"])
def list_courses_by_instructor(instructor_id: str):
    courses = get_courses_by_instructor_id(instructor_id)
    return courses

@router.put("/{id}", response_model=bool, tags=["Courses"])
def update_course_data(id: str, course_data: dict):
    was_updated = update_course(id, course_data)
    if not was_updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return was_updated

@router.delete("/{id}", response_model=bool, tags=["Courses"])
def delete_course_data(id: str):
    was_deleted = delete_course(id)
    if not was_deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return was_deleted