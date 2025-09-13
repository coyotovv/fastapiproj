# 📘 Course Selling API

## 🧠 Project Overview

This project involves building a simple RESTful API for a **course selling platform** using **FastAPI** and **MongoDB**.

The system should support:

- Instructors creating and managing their courses  
- Students browsing and enrolling in courses  
- Basic CRUD operations for all core entities

> 🛠️ No authentication, tests, or CI/CD are required. Keep it clean and minimal.

---

## 🧰 Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** MongoDB (via `pymongo`)  
- **Language:** Python 3.10+  
- **Tools:** Uvicorn (for running server), MongoDB Compass (for DB GUI)

---

## 📦 Folder Structure

```bash
course_api/
├── main.py              # Entry point
├── database.py          # MongoDB connection
├── models/              # Pydantic models
│   ├── instructor.py
│   ├── student.py
│   ├── course.py
│   └── enrollment.py
├── routers/             # Route definitions
│   ├── instructor.py
│   ├── student.py
│   ├── course.py
│   └── enrollment.py
└── crud/                # DB operations
    ├── instructor.py
    ├── student.py
    ├── course.py
    └── enrollment.py


```
---

📚 Entities and Relationships

1. Instructor

Can create multiple courses


2. Course

Belongs to one instructor

Can have many enrolled students


3. Student

Can enroll in many courses


4. Enrollment

Connects a student to a course

Includes timestamp



---

🚏 Endpoints Overview

📘 Instructor

Method	Endpoint	Description
```
GET	/instructors/	List all instructors
POST	/instructors/	Create instructor
GET	/instructors/{id}	Get instructor by ID
PUT	/instructors/{id}	Update instructor
DELETE	/instructors/{id}	Delete instructor
```


---

📕 Course

Method	Endpoint	Description
```
GET	/courses/	List all courses
POST	/courses/	Create a course
GET	/courses/{id}	Get course by ID
PUT	/courses/{id}	Update course
DELETE	/courses/{id}	Delete course
GET	/instructors/{id}/courses/	Get all courses by instructor
```


---

📗 Student

Method	Endpoint	Description
```
GET	/students/	List all students
POST	/students/	Create student
GET	/students/{id}	Get student by ID
PUT	/students/{id}	Update student
DELETE	/students/{id}	Delete student
```


---

📙 Enrollment

Method	Endpoint	Description
```
GET	/enrollments/	List all enrollments
POST	/enrollments/	Enroll a student
DELETE	/enrollments/{id}	Remove enrollment
GET	/students/{id}/courses/	Get student's courses
GET	/courses/{id}/students/	Get course's students
```


---

✅ Deliverables

1. GitHub Repo: Host your complete code in a public repository

Include a README.md with instructions on how to run the project



2. Demo Video (30 seconds max):

Show a short browser demo of:

Creating an instructor, course, student

Enrolling a student in a course

Viewing enrolled students or courses






---

🚀 How to Run

# Step 1: Install dependencies
pip install fastapi uvicorn motor

# Step 2: Run the app
uvicorn main:app --reload
