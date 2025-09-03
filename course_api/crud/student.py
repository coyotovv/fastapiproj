# file: course_api/crud/student.py
from database import db
from models.student import Student
from bson import ObjectId
from models.student import Student

def create_student(student: Student):

    student_dict = student.dict(by_alias=True, exclude_unset=True)
    result = db.students.insert_one(student_dict)
    
    return str(result.inserted_id)

def get_all_students():

    students_cursor = db.students.find({})
    
    return list(students_cursor)

def get_one_student(student_id):

    finding_student = db.students.find_one({"_id": ObjectId(student_id)})
    
    return finding_student