# file: routers/instructor.py
from fastapi import APIRouter, HTTPException
from typing import List
from models.instructor import Instructor
# We need to import all our CRUD functions here.
from crud.instructor import (
    create_instructor,
    get_all_instructors,
    get_instructor_by_id,
    update_instructor,
    delete_instructor
)

router = APIRouter()

@router.post("/", response_model=str, tags=["Instructors"])
def create_new_instructor(instructor: Instructor):
    return create_instructor(instructor)

@router.get("/", response_model=List[Instructor], tags=["Instructors"])
def list_instructors():
    return get_all_instructors()

@router.get("/{id}", response_model=Instructor, tags=["Instructors"])
def get_instructor(id: str):
    instructor = get_instructor_by_id(id)
    if instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor

@router.put("/{id}", response_model=bool, tags=["Instructors"])
def update_instructor(id: str, instructor_data: dict):
    # Call the CRUD function and return its boolean result.
    was_updated = update_instructor(id, instructor_data)
    if not was_updated:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return was_updated

@router.delete("/{id}", response_model=bool, tags=["Instructors"])
def delete_instructor(id: str):
    # Call the CRUD function and return its boolean result.
    was_deleted = delete_instructor(id)
    if not was_deleted:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return was_deleted