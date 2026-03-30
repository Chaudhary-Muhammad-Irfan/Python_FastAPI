from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student")):
    return {
        "message": "Student fetched successfully",
        "student_id": student_id
    }

@app.get("/search")
def search_student(
    name: str = Query(..., min_length=2, description="Student name"),
    age: Optional[int] = Query(None, gt=0, description="Student age (optional)")
):
    return {
        "message": "Search completed",
        "name": name,
        "age": age
    }


class Student(BaseModel):
    name: str
    age: int
    course: str
    is_active: Optional[bool] = True


@app.post("/create-student")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student_data": student
}

@app.put("/update-student/{student_id}")
def update_student(
    student_id: int, 
    notify: bool = Query(False),  
    student: Student = None  
):
    return {
        "message": "Student updated",
        "student_id": student_id,
        "notify_user": notify,
        "updated_data": student
    }