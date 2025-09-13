from fastapi import FastAPI
from routers import instructor, course, student, enrollment


# FastAPI application instance
app = FastAPI(
    title="Course Selling API",
    description="A simple RESTful API for a course selling platform.",
    version="0.1.0"
)

# Include the instructor router
app.include_router(instructor.router)

app.include_router(course.router)

app.include_router(student.router)

app.include_router(enrollment.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Course Selling API!"}