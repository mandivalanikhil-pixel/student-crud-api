
from models.student_model import Student

students = []


def add_student(student):
    students.append(student)
    return student


def get_students():
    return students


def get_student(id):
    for student in students:
        if student.id == id:
            return student
    return None


def update_student(id, student):
    for i in range(len(students)):
        if students[i].id == id:
            student.id = id
            students[i] = student
            return student
    return None


def delete_student(id):
    for i in range(len(students)):
        if students[i].id == id:
            return students.pop(i)
    return None
