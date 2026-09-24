from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI(title="Student Management API")

# MongoDB connection
client = MongoClient("mongodb://127.0.0.1:27017")

db = client["college"]
students_collection = db["students"]


class Student(BaseModel):
    name: str
    age: int
    department: str
    specialization: str


def student_response(student):
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "department": student["department"],
        "specialization": student["specialization"]
    }


@app.get("/")
def home():
    return {"message": "MongoDB FastAPI API is running"}


@app.post("/students")
def create_student(student: Student):
    result = students_collection.insert_one(student.model_dump())

    created_student = students_collection.find_one(
        {"_id": result.inserted_id}
    )

    return student_response(created_student)


@app.get("/students")
def get_students():
    students = students_collection.find()

    return [student_response(student) for student in students]


@app.get("/students/{student_id}")
def get_student(student_id: str):

    try:
        object_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    student = students_collection.find_one({"_id": object_id})

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student_response(student)


@app.put("/students/{student_id}")
def update_student(student_id: str, student: Student):

    try:
        object_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    result = students_collection.update_one(
        {"_id": object_id},
        {"$set": student.model_dump()}
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated_student = students_collection.find_one(
        {"_id": object_id}
    )

    return student_response(updated_student)


@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    try:
        object_id = ObjectId(student_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )

    result = students_collection.delete_one(
        {"_id": object_id}
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }