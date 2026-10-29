
from fastapi import APIRouter, HTTPException, Response
from models.student_model import Student
from controllers.student_controller import *

router = APIRouter()

@router.post("/students", status_code=201)
def add(student: Student):
    return add_student(student)


@router.get("/students")
def get_all():
    return get_students()


@router.get("/students/{id}")
def get_one(id: int):
    student = get_student(id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.put("/students/{id}")
def update(id: int, student: Student):
    result = update_student(id, student)

    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return result


@router.delete("/students/{id}", status_code=204)
def delete(id: int):
    result = delete_student(id)

    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return Response(status_code=204)
