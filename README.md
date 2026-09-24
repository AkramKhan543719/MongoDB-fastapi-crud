# MongoDB + FastAPI CRUD Student Management API

A RESTful Student Management API developed using **FastAPI** and **MongoDB** with **PyMongo**. This project demonstrates how a modern Python API framework can communicate with a NoSQL document database and perform complete CRUD operations.

---

## 📌 Project Overview

This project was developed to explore and implement:

- MongoDB local database setup
- MongoDB databases and collections
- MongoDB documents and BSON
- MongoDB CRUD operations
- FastAPI REST API development
- PyMongo integration
- Pydantic request validation
- MongoDB ObjectId handling
- HTTP status and error handling
- API testing using Swagger UI

The application provides a Student Management API where users can create, retrieve, update, and delete student records stored in MongoDB.

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand MongoDB as a NoSQL document-oriented database.
2. Set up MongoDB locally on Windows.
3. Create and manage MongoDB databases and collections.
4. Perform MongoDB CRUD operations.
5. Integrate MongoDB with FastAPI using PyMongo.
6. Develop RESTful API endpoints.
7. Validate API requests using Pydantic.
8. Handle MongoDB `ObjectId` values.
9. Implement API-level error handling.
10. Test APIs using FastAPI Swagger UI.

---

# 🏗️ System Architecture

```text
                         CLIENT
                           │
                           │ HTTP Request
                           ▼
                  ┌──────────────────┐
                  │     FastAPI      │
                  │   REST API       │
                  └────────┬─────────┘
                           │
                           │ Python Objects
                           ▼
                  ┌──────────────────┐
                  │     PyMongo      │
                  │ MongoDB Driver   │
                  └────────┬─────────┘
                           │
                           │ MongoDB Operations
                           ▼
                  ┌──────────────────┐
                  │     MongoDB      │
                  │  Local Server    │
                  └────────┬─────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    college   │
                    │   Database   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   students   │
                    │  Collection  │
                    └──────────────┘
```

---

## 🧩 Technology Stack

| Technology   | Purpose                        |
|--------------|--------------------------------|
| Python 3.9+  | Programming language           |
| FastAPI      | REST API framework             |
| PyMongo      | MongoDB Python driver          |
| MongoDB 8.3  | NoSQL database                 |
| Pydantic     | Data validation                |
| Uvicorn      | ASGI server                    |
| Swagger UI   | API testing/documentation      |
| PowerShell   | Local development environment  |
| Git          | Version control                |
| GitHub       | Source code hosting            |

---

## 🍃 MongoDB Concepts

### What is MongoDB?

MongoDB is a NoSQL, document-oriented database that stores information in flexible BSON documents instead of traditional relational tables and rows.

Example document:

```json
{
  "_id": "ObjectId(...)",
  "name": "Akram",
  "age": 20,
  "department": "CSE",
  "specialization": "AIML"
}
```

### MongoDB Data Model

```
MongoDB
   │
   └── Database
        │
        └── Collection
              │
              ├── Document
              ├── Document
              └── Document
```

For this project:

```
MongoDB
   │
   └── college
        │
        └── students
              │
              ├── Akram
              ├── Rahul
              └── Vikram
```

### SQL vs MongoDB

| Relational Database | MongoDB                        |
|---------------------|--------------------------------|
| Database            | Database                       |
| Table               | Collection                     |
| Row                 | Document                       |
| Column              | Field                          |
| Primary Key         | `_id`                          |
| JOIN                | `$lookup` / references / embedding |

---

## 🆔 MongoDB ObjectId

MongoDB automatically generates a unique `_id` for every document.

Example:

```
ObjectId("6ab4ed062460da6814cd4b59")
```

The API converts this value into a string before returning it through JSON.

Example API response:

```json
{
  "id": "6ab4ed062460da6814cd4b59",
  "name": "Akram",
  "age": 20,
  "department": "CSE",
  "specialization": "AIML"
}
```

---

## 🔄 CRUD Operations

CRUD stands for:

- **C** → Create
- **R** → Read
- **U** → Update
- **D** → Delete

### Create

MongoDB:

```js
db.students.insertOne({
    name: "Akram",
    age: 20,
    department: "CSE",
    specialization: "AIML"
})
```

FastAPI:

```
POST /students
```

### Read

MongoDB:

```js
db.students.find()
```

FastAPI:

```
GET /students
```

### Update

MongoDB:

```js
db.students.updateOne(
    { name: "Akram" },
    { $set: { age: 21 } }
)
```

FastAPI:

```
PUT /students/{student_id}
```

### Delete

MongoDB:

```js
db.students.deleteOne({
    name: "Akram"
})
```

FastAPI:

```
DELETE /students/{student_id}
```

---

## 🔌 API Architecture

```
Client
  │
  ├── POST /students
  │
  ├── GET /students
  │
  ├── GET /students/{id}
  │
  ├── PUT /students/{id}
  │
  └── DELETE /students/{id}
  │
  ▼
FastAPI
  │
  ▼
Pydantic Validation
  │
  ▼
PyMongo
  │
  ▼
MongoDB
```

---

## 📡 API Endpoints

| Method | Endpoint                    | Description           |
|--------|-----------------------------|-----------------------|
| POST   | `/students`                 | Create a student      |
| GET    | `/students`                 | Retrieve all students |
| GET    | `/students/{student_id}`    | Retrieve a student    |
| PUT    | `/students/{student_id}`    | Update a student      |
| DELETE | `/students/{student_id}`    | Delete a student      |

---

## 📝 API Examples

### 1. Create Student

**Request**

```
POST /students
```

```json
{
  "name": "Vikram",
  "age": 22,
  "department": "CSE",
  "specialization": "AI"
}
```

**Response**

```json
{
  "id": "6ab4eed5ab59a7f2b5f2e2c3",
  "name": "Vikram",
  "age": 22,
  "department": "CSE",
  "specialization": "AI"
}
```

### 2. Get All Students

```
GET /students
```

Example response:

```json
[
  {
    "id": "6ab4ed062460da6814cd4b59",
    "name": "Akram",
    "age": 20,
    "department": "CSE",
    "specialization": "AIML"
  },
  {
    "id": "6ab4ed192460da6814cd4b5a",
    "name": "Rahul",
    "age": 20,
    "department": "CSE",
    "specialization": "AIML"
  }
]
```

### 3. Get Student by ID

```
GET /students/{student_id}
```

Example:

```
GET /students/6ab4ed062460da6814cd4b59
```

### 4. Update Student

```
PUT /students/{student_id}
```

Request:

```json
{
  "name": "Akram Updated",
  "age": 21,
  "department": "CSE",
  "specialization": "Data Science"
}
```

### 5. Delete Student

```
DELETE /students/{student_id}
```

Response:

```json
{
  "message": "Student deleted successfully"
}
```

---

## ⚠️ Error Handling

The API handles invalid MongoDB IDs.

Example:

```
PUT /students/3
```

Response:

```json
{
  "detail": "Invalid student ID"
}
```

HTTP Status:

```
400 Bad Request
```

If a valid ObjectId does not exist:

```
404 Not Found
```

Example:

```json
{
  "detail": "Student not found"
}
```

This ensures the API does not expose raw database errors to the client.

---

## 📁 Project Structure

```
mongodb-fastapi-crud/
│
├── main.py
├── requirements.txt
├── .gitignore
└── venv/                  # Local only, not committed
```

---

## ⚙️ MongoDB Configuration

The application connects to the local MongoDB server using:

```python
MongoClient("mongodb://127.0.0.1:27017")
```

Database:

```
college
```

Collection:

```
students
```

Architecture:

```
mongodb://127.0.0.1:27017
              │
              ▼
           college
              │
              ▼
          students
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/AkramKhan543719/MongoDB-fastapi-crud.git
cd MongoDB-fastapi-crud
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 🗄️ Start MongoDB

Make sure the MongoDB Windows service is running.

Check using PowerShell:

```powershell
Get-Service MongoDB
```

Expected:

```
Status   Name      DisplayName
Running  MongoDB   MongoDB Server (MongoDB)
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📚 Swagger Documentation

FastAPI automatically provides interactive API documentation.

Open:

```
http://127.0.0.1:8000/docs
```

Alternative:

```
http://127.0.0.1:8000/redoc
```

---

## 🧪 Testing

The CRUD operations were tested using FastAPI Swagger UI.

Test flow:

```
POST
 ↓
Create Student
 ↓
GET
 ↓
Verify Student
 ↓
PUT
 ↓
Update Student
 ↓
GET
 ↓
Verify Update
 ↓
DELETE
 ↓
Remove Student
 ↓
GET
 ↓
Verify Deletion
```

Additional negative testing was performed using:

- Invalid MongoDB ObjectId
- Non-existent student ID
- Repeated deletion of an already deleted document

---

## ✅ Validation Results

The following operations were successfully tested:

```
MongoDB Local Setup             ✅
MongoDB Connection              ✅
Database Creation               ✅
Collection Creation             ✅
Insert One                      ✅
Insert Many                     ✅
Read Documents                  ✅
Filtered Read                   ✅
Update Document                 ✅
Delete Document                 ✅
FastAPI Integration             ✅
POST /students                  ✅
GET /students                   ✅
GET /students/{id}              ✅
PUT /students/{id}              ✅
DELETE /students/{id}           ✅
Invalid ObjectId Handling       ✅
404 Not Found Handling          ✅
Swagger API Testing             ✅
```

---

## 🔐 Security Considerations

This project is intended for local development and learning.

For production use, the following should be implemented:

- MongoDB authentication
- Environment variables for credentials
- HTTPS
- API authentication and authorization
- Input validation and sanitization
- Rate limiting
- Secure secret management
- Production database configuration
- Logging and monitoring

The local development MongoDB instance used during exploration had authentication disabled.

---

## 🔮 Future Improvements

Potential improvements include:

- JWT authentication
- Role-based access control
- Pagination
- Search and filtering
- Sorting
- MongoDB indexes
- Async database operations
- Docker deployment
- Unit and integration tests
- Automated CI/CD
- Production MongoDB authentication
- Environment-based configuration
- API versioning

---

## 🎓 Learning Outcomes

Through this project, the following concepts were explored:

- NoSQL databases
- Document-oriented data modeling
- MongoDB databases and collections
- BSON documents
- MongoDB ObjectId
- MongoDB CRUD
- PyMongo
- FastAPI
- Pydantic
- REST APIs
- HTTP methods
- API validation
- HTTP status codes
- Exception handling
- Swagger/OpenAPI
- Git and GitHub

---

## 👨‍💻 Author

**Pathan Mohammed Akram Khan**

B.Tech — Computer Science & Engineering (AI/ML)

GitHub: [https://github.com/AkramKhan543719](https://github.com/AkramKhan543719)

---

## 📄 License

This project was developed for educational and internship learning purposes.