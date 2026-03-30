from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

Students = {
    1: {
        "name": "John",
        "age": 20,
        "city": "New York"
    },
    2: {
        "name": "Jane",
        "age": 21,
        "city": "Los Angeles"
    },
    3: {
        "name": "Jim",
        "age": 22,
        "city": "Chicago"
    }
}

class Student(BaseModel):
    name: str
    age: int
    city: Optional[str] = None

@app.get("/get_students")
def get_students():
    return {"message": "Hello World"}

@app.get("/get_student_by_id/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student")):
    return Students[student_id] if student_id in Students else {"message": "Student not found"}

@app.post("/create_student")
def create_student(student: Student):
    Students[len(Students) + 1] = student
    return Students

@app.put("/update_student/{student_id}")
def update_student(student_id: int, student: Student):
    Students[student_id] = student
    return Students

@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    Students.pop(student_id)
    return Students

