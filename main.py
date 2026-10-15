from fastapi import FastAPI, HTTPException

app = FastAPI()

students = [
    {"id": 1, "name": "a", "dept": "python"},
    {"id": 2, "name": "b", "dept": "c"},
    {"id": 3, "name": "c", "dept": "java"},
    {"id": 4, "name": "d", "dept": "python"},
    {"id": 5, "name": "e", "dept": "c"}
]

@app.get("/students/{student_id}")
def get_student_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    # Raise a 404 error if the student ID is not found
    raise HTTPException(status_code=404, detail="Student ID is invalid")

@app.get("/students")
def get_student_dept(dept: str | None = None):
    # If no department is passed, return all students
    if dept is None:
        return students
        
    result = []
    for student in students:
        if student["dept"].lower() == dept.lower():
            result.append(student)
            
    return result