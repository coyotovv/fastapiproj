# file: crud/student.py
from database import db
from models.student import Student
from bson import ObjectId

def create_student(student: Student):
    student_dict = student.dict(by_alias=True, exclude_unset=True)
    result = db.students.insert_one(student_dict)
    return str(result.inserted_id)

def get_all_students():
    students_cursor = db.students.find({})
    return list(students_cursor)

def get_one_student(student_id: str):
    found_student = db.students.find_one({"_id": ObjectId(student_id)})
    return found_student

def update_student(student_id: str, student_data: dict):
    result = db.students.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student_data}
    )
    return result.modified_count > 0

def delete_student(student_id: str):
    result = db.students.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0