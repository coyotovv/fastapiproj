# file: crud/instructor.py
from database import db
from models.instructor import Instructor
from bson import ObjectId

def create_instructor(instructor: Instructor):
    instructor_dict = instructor.dict(by_alias=True, exclude_unset=True)
    result = db.instructors.insert_one(instructor_dict)
    return str(result.inserted_id)

def get_all_instructors():
    instructors_cursor = db.instructors.find({})
    return list(instructors_cursor)

def get_instructor_by_id(instructor_id: str):
    found_instructor = db.instructors.find_one({"_id": ObjectId(instructor_id)})
    return found_instructor

def update_instructor(instructor_id: str, instructor_data: dict):
    result = db.instructors.update_one(
        {"_id": ObjectId(instructor_id)},
        {"$set": instructor_data}
    )
    return result.modified_count > 0

def delete_instructor(instructor_id: str):
    result = db.instructors.delete_one({"_id": ObjectId(instructor_id)})
    return result.deleted_count > 0