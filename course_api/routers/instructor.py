from fastapi import APIRouter, status
from bson import ObjectId
from pydantic import BaseModel
from models.instructor import Instructor
from database import db
from pymongo import ReturnDocument


router = APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)


class InstructorOut(BaseModel):
    id: str
    name: str
    email: str
    bio: str | None = None



@router.post("/", response_model=InstructorOut, status_code=status.HTTP_201_CREATED)
def create_instructor(instructor: Instructor):
    instructor_dict = instructor.dict()

    result = db.instructors.insert_one(instructor_dict)
    

    return {
        "id": str(result.inserted_id),
        **instructor.dict()
    }





@router.put("/{id}", response_model=InstructorOut)
def update_instructor(id: str, instructor: Instructor):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid instructor ID format")

    updated_instructor = db.instructors.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": instructor.dict()},
        return_document=ReturnDocument.AFTER
    )
    
    if updated_instructor:

        updated_instructor["id"] = str(updated_instructor["_id"])

        updated_instructor.pop("_id")
        return updated_instructor
    else:
        raise HTTPException(status_code=404, detail="Instructor not found")





@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_instructor(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid instructor ID format")

    deleted_instructor = db.instructors.find_one_and_delete({"_id": ObjectId(id)})
    if not deleted_instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")

    return None