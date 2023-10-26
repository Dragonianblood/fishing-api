from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Student(BaseModel):
    name: str
    grade: int
    gpa: float = 0.0
    nehs: Optional[bool] = False


students = [
    Student(name="a", grade=10, gpa=3.5),
    Student(name="b", grade=11, gpa=3.2),
    Student(name="c", grade=9, gpa=4.0)
]


@router.get("/")
async def get_all_academics():
    return students


@router.post("/")
async def add_new_student(student: Student):
    students.append(student)
    print(student)
    return {"msg": "student added"}


@router.get("/{student_name}")
async def get_student_academic_record(student_name: str):
    for student in students:
        if student_name.lower() in student.name.lower():
            return student
    return {"msg": f"{student_name} has a great record"}
