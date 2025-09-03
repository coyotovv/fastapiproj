# file: crud/course.py
from database import db
from models.course import Course
from bson import ObjectId

def create_course(course: Course):
    """Inserts a new course document into the database."""
    course_dict = course.dict(by_alias=True, exclude_unset=True)
    result = db.courses.insert_one(course_dict)
    return str(result.inserted_id)

def get_all_courses():
    """Retrieves all course documents from the database."""
    courses_cursor = db.courses.find({})
    return list(courses_cursor)

def get_course_by_id(course_id: str):
    """Retrieves a single course by its ID."""
    found_course = db.courses.find_one({"_id": ObjectId(course_id)})
    return found_course

def get_courses_by_instructor_id(instructor_id: str):
    """Retrieves all courses for a specific instructor."""
    # We query the 'courses' collection for documents where the 'instructor_id' matches.
    courses_cursor = db.courses.find({"instructor_id": instructor_id})
    return list(courses_cursor)

def update_course(course_id: str, course_data: dict):
    """Updates an existing course document."""
    # The `$set` operator is used to update fields within a document.
    result = db.courses.update_one(
        {"_id": ObjectId(course_id)},
        {"$set": course_data}
    )
    return result.modified_count > 0

def delete_course(course_id: str):
    """Deletes a single course document."""
    result = db.courses.delete_one({"_id": ObjectId(course_id)})
    return result.deleted_count > 0