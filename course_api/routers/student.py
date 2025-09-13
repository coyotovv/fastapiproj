from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from bson import ObjectId
from database import db
from models.student import Student
from typing import Optional
from pymongo import ReturnDocument



router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

class StudentOut(BaseModel):
    id: str
    name: str
    email: str
    bio: Optional[str] = None



@router.post("/", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    student_dict = student.dict()
    result = db.students.insert_one(student_dict)
    student_dict["id"] = str(result.inserted_id)
    return student_dict


@router.get("/")
def list_students():
    students = list(db.students.find({}))
    for student in students:
        student["id"] = str(student["_id"])
        student.pop("_id") 
    return students

@router.get("/{id}")
def get_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    student = db.students.find_one({"_id": ObjectId(id)})
    if student:
        student["id"] = str(student["_id"])
        student.pop("_id") 
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@router.put("/{id}", response_model=StudentOut)
def update_student(id: str, student: Student):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    updated_student = db.students.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": student.dict()},
        return_document=ReturnDocument.AFTER
    )
    
    if updated_student:
        updated_student["id"] = str(updated_student["_id"])
        updated_student.pop("_id")
        return updated_student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    deleted_student = db.students.find_one_and_delete({"_id": ObjectId(id)})
    if not deleted_student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    return None