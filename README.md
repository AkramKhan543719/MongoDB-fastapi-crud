\# 🚀 MongoDB + FastAPI CRUD API



A complete hands-on project exploring \*\*MongoDB\*\* with \*\*FastAPI\*\*, covering local MongoDB setup, MongoDB concepts, and full CRUD operations for a `students` resource.



\---



\## 📌 Overview



This project is a deep-dive into building a modern, high-performance REST API using \*\*FastAPI\*\* backed by \*\*MongoDB\*\*. It demonstrates:



\- Local MongoDB installation \& verification

\- MongoDB Compass usage for GUI-based CRUD

\- Connecting FastAPI to MongoDB using \*\*PyMongo / Motor\*\*

\- Building a clean CRUD REST API with \*\*Pydantic\*\* models

\- Async database operations with \*\*Motor\*\*

\- Testing endpoints via \*\*Swagger UI\*\* and \*\*Postman\*\*



\---



\## 🧰 Tech Stack



| Layer        | Technology            |

|--------------|------------------------|

| Database     | MongoDB                |

| GUI Tool     | MongoDB Compass        |

| Backend      | FastAPI                |

| Driver       | PyMongo / Motor (async)|

| Validation   | Pydantic               |

| ASGI Server  | Uvicorn                |

| Testing      | Swagger UI, Postman    |



\---



\## 🧠 MongoDB Concepts Covered



\### 1. Document-Oriented Storage

MongoDB stores data as \*\*BSON documents\*\* (Binary JSON) instead of rows in tables.



```json

{

&#x20; "\_id": ObjectId("..."),

&#x20; "name": "Akram Khan",

&#x20; "age": 22,

&#x20; "course": "Computer Science"

}

```



\### 2. Database → Collection → Document Hierarchy

| SQL        | MongoDB     |

|------------|-------------|

| Database   | Database    |

| Table      | Collection  |

| Row        | Document    |

| Column     | Field       |

| JOIN       | `$lookup`   |



\### 3. `\_id` and ObjectId

Every document has a unique `\_id` (auto-generated `ObjectId` if not provided). This is MongoDB's equivalent of a primary key.



\### 4. Schema-less / Flexible Schema

Collections don't enforce a fixed schema — different documents can have different fields. Validation is done at the \*\*application layer\*\* (Pydantic in FastAPI).



\### 5. CRUD Operations in MongoDB

```js

db.students.insertOne({ name: "Akram", age: 22 })

db.students.find({ age: { $gt: 20 } })

db.students.updateOne({ name: "Akram" }, { $set: { age: 23 } })

db.students.deleteOne({ name: "Akram" })

```



\### 6. Indexing

Indexes speed up queries. MongoDB auto-creates an index on `\_id`. Custom indexes:

```js

db.students.createIndex({ name: 1 })

```



\### 7. Aggregation Pipeline

Powerful data processing: `$match → $group → $sort → $project`



\---



\## 🧠 FastAPI Concepts Covered



\### 1. ASGI \& Async Support

FastAPI runs on ASGI (Uvicorn) and supports `async/await` natively — perfect for \*\*Motor\*\* (async MongoDB driver).



\### 2. Pydantic Models

Used for request/response validation and serialization.



```python

class Student(BaseModel):

&#x20;   name: str

&#x20;   age: int

&#x20;   course: str

```



\### 3. Dependency Injection

FastAPI's `Depends()` injects DB connections, auth, etc., cleanly.



\### 4. Automatic Docs

\- Swagger UI → `/docs`

\- ReDoc → `/redoc`



\### 5. Path \& Query Parameters

```python

@app.get("/students/{id}")

async def get\_student(id: str): ...

```



\### 6. Response Models

Use `response\_model=StudentOut` to shape output \& hide sensitive fields.



\---



\## 🔄 Flow Diagram



```

┌──────────────┐

│   Client     │  (Swagger / Postman / Browser)

└──────┬───────┘

&#x20;      │ HTTP Request (JSON)

&#x20;      ▼

┌──────────────────────┐

│   FastAPI (Uvicorn)  │

│  ┌────────────────┐  │

│  │  Pydantic      │  │  ← Validation

│  │  Validation    │  │

│  └───────┬────────┘  │

│          ▼            │

│  ┌────────────────┐  │

│  │  Route Handler │  │

│  └───────┬────────┘  │

└──────────┼───────────┘

&#x20;          │ Motor (async driver)

&#x20;          ▼

┌──────────────────────┐

│   MongoDB Server     │

│   ┌──────────────┐   │

│   │  Database    │   │

│   │  └ Collection│   │

│   │     └ Doc    │   │

│   └──────────────┘   │

└──────────────────────┘

&#x20;          │

&#x20;          ▼

&#x20;    JSON Response

&#x20;          │

&#x20;          ▼

┌──────────────┐

│   Client     │

└──────────────┘

```



\---



\## 📁 Project Structure



```

mongodb-fastapi/

│

├── main.py               # FastAPI app entry point

├── database.py           # MongoDB connection (Motor)

├── models.py             # Pydantic models

├── routes/

│   └── students.py       # CRUD routes for students

├── requirements.txt

├── .gitignore

└── README.md

```



\---



\## ⚙️ Setup Instructions



\### 1. Install MongoDB Locally

\- Download \*\*MongoDB Community Server\*\*

\- Install \*\*MongoDB Compass\*\* (GUI)

\- Start the MongoDB service

\- Verify: `mongodb://localhost:27017`



\### 2. Clone the Repository

```bash

git clone https://github.com/AkramKhan543719/mongodb-fastapi.git

cd mongodb-fastapi

```



\### 3. Create Virtual Environment

```bash

python -m venv venv

venv\\Scripts\\activate      # Windows

source venv/bin/activate   # macOS/Linux

```



\### 4. Install Dependencies

```bash

pip install -r requirements.txt

```



\### 5. Run the Server

```bash

uvicorn main:app --reload

```



\- Server → `http://127.0.0.1:8000`

\- Swagger UI → `http://127.0.0.1:8000/docs`



\---



\## 🔗 API Endpoints



| Method | Endpoint          | Description              |

|--------|-------------------|--------------------------|

| POST   | `/students`       | Create a new student     |

| GET    | `/students`       | Get all students         |

| GET    | `/students/{id}`  | Get a student by ID      |

| PUT    | `/students/{id}`  | Update a student by ID   |

| DELETE | `/students/{id}`  | Delete a student by ID   |



\### Example Request Body



```json

{

&#x20; "name": "Akram Khan",

&#x20; "age": 22,

&#x20; "course": "Computer Science"

}

```



\---



\## 🧪 Testing



\- \*\*Swagger UI\*\* → `http://127.0.0.1:8000/docs`

\- \*\*Postman\*\* → Import and test each endpoint manually



\---



\## ✅ What I Learned



\- MongoDB's document model vs traditional SQL tables

\- Async MongoDB operations with \*\*Motor\*\*

\- Structuring FastAPI apps with routers and Pydantic

\- Handling `ObjectId` serialization in API responses

\- Testing APIs efficiently with Swagger \& Postman



\---



\## 👤 Author



\*\*Pathan Mohammed Akram Khan\*\*

🔗 GitHub: \[@AkramKhan543719](https://github.com/AkramKhan543719)

