


API Operations Reference GuideThis document contains a complete list of all the endpoints for the Course Selling API. Use this as a quick reference for testing and interacting with your API using PowerShell.








👨‍🏫 Instructors1. Create an InstructorMethod: POSTURL: /instructors/Description: Creates a new instructor.Invoke-WebRequest -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"name": "Jane Doe", "email": "jane.doe@example.com", "bio": "A passionate instructor."}' -Uri '[http://127.0.0.1:8000/instructors/](http://127.0.0.1:8000/instructors/)'


2. List All InstructorsMethod: GETURL: /instructors/Description: Retrieves a list of all instructors.Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/instructors/](http://127.0.0.1:8000/instructors/)'


3. Get Instructor by IDMethod: GETURL: /instructors/{id}Description: Retrieves a single instructor by their unique ID.# Replace <ID> with a valid instructor ID
Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/instructors/](http://127.0.0.1:8000/instructors/)<ID>'


4. Update an InstructorMethod: PUTURL: /instructors/{id}Description: Updates the details of an existing instructor.# Replace <ID> with a valid instructor ID
Invoke-WebRequest -Method PUT -Headers @{"Content-Type" = "application/json"} -Body '{"name": "Jane Doe", "email": "jane.doe@newemail.com", "bio": "Updated bio."}' -Uri '[http://127.0.0.1:8000/instructors/](http://127.0.0.1:8000/instructors/)<ID>'


5. Delete an InstructorMethod: DELETEURL: /instructors/{id}Description: Deletes an instructor document.# Replace <ID> with a valid instructor ID
Invoke-WebRequest -Method DELETE -Uri '[http://127.0.0.1:8000/instructors/](http://127.0.0.1:8000/instructors/)<ID>' -UseBasicParsing







📚 Courses1. Create a CourseMethod: POSTURL: /courses/Description: Creates a new course and links it to an instructor.# Replace <instructor_id> with a valid instructor ID
Invoke-WebRequest -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"title": "Intro to API", "description": "Learn the basics of API development.", "instructor_id": "<instructor_id>"}' -Uri '[http://127.0.0.1:8000/courses/](http://127.0.0.1:8000/courses/)'


2. List All CoursesMethod: GETURL: /courses/Description: Retrieves a list of all courses.Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/courses/](http://127.0.0.1:8000/courses/)'


3. Get Course by IDMethod: GETURL: /courses/{id}Description: Retrieves a single course by its unique ID.# Replace <ID> with a valid course ID
Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/courses/](http://127.0.0.1:8000/courses/)<ID>'


4. Update a CourseMethod: PUTURL: /courses/{id}Description: Updates the details of an existing course.# Replace <ID> with a valid course ID
Invoke-WebRequest -Method PUT -Headers @{"Content-Type" = "application/json"} -Body '{"title": "Updated Course Title", "description": "New description.", "instructor_id": "<instructor_id>"}' -Uri '[http://127.0.0.1:8000/courses/](http://127.0.0.1:8000/courses/)<ID>'


5. Delete a CourseMethod: DELETEURL: /courses/{id}Description: Deletes a course document.# Replace <ID> with a valid course ID
Invoke-WebRequest -Method DELETE -Uri '[http://127.0.0.1:8000/courses/](http://127.0.0.1:8000/courses/)<ID>' -UseBasicParsing






🎓 Students1. Create a StudentMethod: POSTURL: /students/Description: Creates a new student.Invoke-WebRequest -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"name": "John Smith", "email": "john.smith@example.com", "bio": "A passionate student."}' -Uri '[http://127.0.0.1:8000/students/](http://127.0.0.1:8000/students/)'


2. List All StudentsMethod: GETURL: /students/Description: Retrieves a list of all students.Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/students/](http://127.0.0.1:8000/students/)'


3. Get Student by IDMethod: GETURL: /students/{id}Description: Retrieves a single student by their unique ID.# Replace <ID> with a valid student ID
Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/students/](http://127.0.0.1:8000/students/)<ID>'


4. Update a StudentMethod: PUTURL: /students/{id}Description: Updates the details of an existing student.# Replace <ID> with a valid student ID
Invoke-WebRequest -Method PUT -Headers @{"Content-Type" = "application/json"} -Body '{"name": "Jane Smith", "email": "jane.smith@example.com", "bio": "Updated bio."}' -Uri '[http://127.0.0.1:8000/students/](http://127.0.0.1:8000/students/)<ID>'


5. Delete a StudentMethod: DELETEURL: /students/{id}Description: Deletes a student document.# Replace <ID> with a valid student ID
Invoke-WebRequest -Method DELETE -Uri '[http://127.0.0.1:8000/students/](http://127.0.0.1:8000/students/)<ID>' -UseBasicParsing






📝 Enrollments1. Create an EnrollmentMethod: POSTURL: /enrollments/Description: Enrolls a single student in a single course.# Replace <student_id> and <course_id> with valid IDs
Invoke-WebRequest -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"student_id": "<student_id>", "course_id": "<course_id>"}' -Uri '[http://127.0.0.1:8000/enrollments/](http://127.0.0.1:8000/enrollments/)'


2. Bulk Enroll StudentsMethod: POSTURL: /enrollments/bulk/Description: Enrolls multiple students in a single course.# Replace <student_id_1>, <student_id_2>, and <course_id> with valid IDs
Invoke-WebRequest -Method POST -Headers @{"Content-Type" = "application/json"} -Body '{"student_ids": ["<student_id_1>", "<student_id_2>"], "course_id": "<course_id>"}' -Uri '[http://127.0.0.1:8000/enrollments/bulk/](http://127.0.0.1:8000/enrollments/bulk/)'


3. Get a Student's CoursesMethod: GETURL: /enrollments/students/{id}/courses/Description: Retrieves a list of all courses a student is enrolled in.# Replace <ID> with a valid student ID
Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/enrollments/students/](http://127.0.0.1:8000/enrollments/students/)<ID>/courses/'


4. Get a Course's StudentsMethod: GETURL: /enrollments/courses/{id}/students/Description: Retrieves a list of all students enrolled in a specific course.# Replace <ID> with a valid course ID
Invoke-WebRequest -Method GET -Uri '[http://127.0.0.1:8000/enrollments/courses/](http://127.0.0.1:8000/enrollments/courses/)<ID>/students/'


5. Delete an EnrollmentMethod: DELETEURL: /enrollments/{id}Description: Deletes a single enrollment document.# Replace <ID> with a valid enrollment ID
Invoke-WebRequest -Method DELETE -Uri '[http://127.0.0.1:8000/enrollments/](http://127.0.0.1:8000/enrollments/)<ID>' -UseBasicParsing

