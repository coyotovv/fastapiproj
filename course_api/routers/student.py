# file: routers/student.py
from fastapi import APIRouter, HTTPException
from typing import List
from models.student import Student
# Import all the CRUD functions for the student resource
from crud.student import (
    create_student,
    get_all_students,
    get_one_student,
    update_student,
    delete_student
)

router = APIRouter()

@router.post("/", response_model=str, tags=["Students"])
def create_new_student(student: Student):
    # Calls the create function and returns the ID
    return create_student(student)

@router.get("/", response_model=List[Student], tags=["Students"])
def list_students():
    # Calls the get all function and returns the list
    return get_all_students()

@router.get("/{id}", response_model=Student, tags=["Students"])
def get_student(id: str):
    # Calls the get one function
    student = get_one_student(id)
    # Checks if the student exists and raises a 404 error if not
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{id}", response_model=bool, tags=["Students"])
def update_student_data(id: str, student_data: dict):
    # Calls the update function
    was_updated = update_student(id, student_data)
    # Checks the boolean result and raises a 404 if not updated
    if not was_updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return was_updated

@router.delete("/{id}", response_model=bool, tags=["Students"])
def delete_student_data(id: str):
    # Calls the delete function
    was_deleted = delete_student(id)
    # Checks the boolean result and raises a 404 if not deleted
    if not was_deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return was_deleted