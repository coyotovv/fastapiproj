from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from database import db
from models.course import Course
from typing import Optional
from datetime import datetime
from pymongo import ReturnDocument

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

class CourseOut(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    instructor_id: str
    creation_date: datetime

@router.post("/", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
def create_course(course: Course):

    course_dict = course.dict()
    
    result = db.courses.insert_one(course_dict)

    course_dict["id"] = str(result.inserted_id)
    
    return course_dict


@router.put("/{id}", response_model=CourseOut)
def update_course(id: str, course: Course):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid course ID format")

    updated_course = db.courses.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": course.dict()},
        return_document=ReturnDocument.AFTER
    )
    
    if updated_course:
        updated_course["id"] = str(updated_course["_id"])
        updated_course.pop("_id")
        return updated_course
    else:
        raise HTTPException(status_code=404, detail="Course not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid course ID format")

    deleted_course = db.courses.find_one_and_delete({"_id": ObjectId(id)})
    if not deleted_course:
        raise HTTPException(status_code=404, detail="Course not found")

    return None


@router.get("/")
def list_courses():
    courses = list(db.courses.find({}))
    

    for course in courses:
        course["id"] = str(course["_id"])
        course.pop("_id")

    return courses