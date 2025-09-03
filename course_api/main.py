# file: main.py
from fastapi import FastAPI
# Import all the routers we have created
from routers import instructor, student, course, enrollment

# Create the main FastAPI application instance
app = FastAPI(
    title="Course Selling API",
    description="A simple RESTful API for a course selling platform."
)

# Include all the routers, linking them to a specific URL prefix.
# This makes it so all our /instructors routes are handled by the
# 'instructor' router, and so on.
app.include_router(instructor.router, prefix="/instructors")
app.include_router(student.router, prefix="/students")
app.include_router(course.router, prefix="/courses")
app.include_router(enrollment.router, prefix="/enrollments")

# A simple root endpoint to confirm the API is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Course Selling API! 🏍️"}