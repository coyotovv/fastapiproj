# file: crud/enrollment.py
from database import db
from models.enrollment import Enrollment
from bson import ObjectId

def create_enrollment(enrollment: Enrollment):
    """Creates a new enrollment document."""
    enrollment_dict = enrollment.dict(by_alias=True, exclude_unset=True)
    result = db.enrollments.insert_one(enrollment_dict)
    return str(result.inserted_id)

def get_all_enrollments():
    """Retrieves all enrollment documents."""
    enrollments_cursor = db.enrollments.find({})
    return list(enrollments_cursor)

def delete_enrollment(enrollment_id: str):
    """Deletes a single enrollment document."""
    result = db.enrollments.delete_one({"_id": ObjectId(enrollment_id)})
    return result.deleted_count > 0

def get_students_by_course(course_id: str):
    """Retrieves all enrollment documents for a specific course."""
    enrollments_cursor = db.enrollments.find({"course_id": course_id})
    return list(enrollments_cursor)

def get_courses_by_student(student_id: str):
    """Retrieves all enrollment documents for a specific student."""
    enrollments_cursor = db.enrollments.find({"student_id": student_id})
    return list(enrollments_cursor)