from fastapi import APIRouter, status
from bson import ObjectId
from pydantic import BaseModel
from models.instructor import Instructor
from database import db
from pymongo import ReturnDocument

# APIRouter for defining our endpoints
router = APIRouter(
    prefix="/instructors",
    tags=["Instructors"]
)

# Pydantic model for response (so we don't return the MongoDB ObjectId)
class InstructorOut(BaseModel):
    id: str
    name: str
    email: str
    bio: str | None = None





# POST endpoint to create a new instructor
@router.post("/", response_model=InstructorOut, status_code=status.HTTP_201_CREATED)
def create_instructor(instructor: Instructor):
    instructor_dict = instructor.dict()
    # Insert the new instructor document into the 'instructors' collection
    result = db.instructors.insert_one(instructor_dict)
    
    # Return the newly created instructor data with the generated ID
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
        # Convert the MongoDB ObjectId to a string before returning
        updated_instructor["id"] = str(updated_instructor["_id"])
        # Remove the ObjectId field from the dictionary
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

    return None # We return None for 204 No Content status