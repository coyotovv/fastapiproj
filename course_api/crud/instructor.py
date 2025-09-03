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