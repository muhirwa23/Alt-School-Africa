# 🎓 EduTrack Lite API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688.svg?style=flat&logo=FastAPI)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB.svg?style=flat&logo=Python)](https://python.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.11.7-E92063.svg?style=flat&logo=Pydantic)](https://pydantic.dev/)

A modern, fast, and comprehensive FastAPI-based system for managing course enrollments and tracking course completion. Built with clean architecture, full validation, and comprehensive testing.

## ✨ Features

### 🚀 **Core Functionality**
- **👤 User Management**: Complete CRUD operations with user deactivation
- **🗓️ Course Management**: Full course lifecycle with enrollment control
- **📝 Enrollment Management**: Smart enrollment with business rule validation
- **📊 Real-time Data**: In-memory storage with automatic example data loading

### 🛡️ **Quality & Security**
- **✅ Data Validation**: Pydantic models with comprehensive validation
- **🧪 Comprehensive Testing**: 25+ test cases covering all scenarios
- **📚 Auto Documentation**: Interactive API docs with Swagger UI
- **🔒 Business Rules**: Enforced validation for data integrity

### 🎯 **Developer Experience**
- **📖 Clear Documentation**: Detailed README with examples
- **🔧 Easy Setup**: One-command installation and startup
- **🚀 Hot Reload**: Development server with auto-reload
- **📋 Example Data**: Pre-loaded with realistic test data

## 🏗️ Project Structure

```
📁 EduTrack Lite API/
├── 📄 main.py                    # 🚀 FastAPI application entry point
├── 📄 run_server.py              # 🎮 Easy server startup script
├── 📄 requirements.txt           # 📦 Python dependencies
├── 📄 test_api.py               # 🧪 Comprehensive test suite
├── 📄 README.md                 # 📚 This documentation
├── 📁 schemas/                  # 📋 Pydantic data models
│   ├── 📄 __init__.py
│   ├── 📄 user.py              # 👤 User data schemas
│   ├── 📄 course.py            # 🗓️ Course data schemas
│   └── 📄 enrollment.py        # 📝 Enrollment data schemas
├── 📁 routes/                   # 🛣️ API route handlers
│   ├── 📄 __init__.py
│   ├── 📄 users.py             # 👤 User endpoints
│   ├── 📄 courses.py           # 🗓️ Course endpoints
│   └── 📄 enrollments.py       # 📝 Enrollment endpoints
└── 📁 services/                 # ⚙️ Business logic layer
    ├── 📄 __init__.py
    ├── 📄 database.py          # 💾 In-memory data storage
    ├── 📄 user_service.py      # 👤 User business logic
    ├── 📄 course_service.py    # 🗓️ Course business logic
    └── 📄 enrollment_service.py # 📝 Enrollment business logic
```

## 🚀 Quick Start

### 📋 Prerequisites
- Python 3.8+ (tested with Python 3.13)
- pip package manager

### ⚡ Installation & Setup

1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn pytest httpx email-validator
   ```
   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server** (choose one method):

   **Method 1: Easy startup script** (recommended)
   ```bash
   python run_server.py
   ```

   **Method 2: Direct FastAPI**
   ```bash
   python main.py
   ```

   **Method 3: Uvicorn directly**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **🎉 You're ready!** The API is now running at `http://localhost:8000`

### 📚 API Documentation

Once the server is running, access these documentation interfaces:

| Interface | URL | Description |
|-----------|-----|-------------|
| 🎮 **Interactive Docs** | `http://localhost:8000/docs` | Swagger UI - Test endpoints directly |
| 📖 **ReDoc** | `http://localhost:8000/redoc` | Beautiful alternative documentation |
| 📋 **OpenAPI JSON** | `http://localhost:8000/openapi.json` | Raw OpenAPI specification |
| 🏠 **API Root** | `http://localhost:8000/` | Welcome message and endpoint overview |
| ❤️ **Health Check** | `http://localhost:8000/health` | Server health status |

## 🛣️ API Endpoints

### 👤 User Management

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| `POST` | `/users/` | Create a new user | `201 Created` |
| `GET` | `/users/` | Get all users | `200 OK` |
| `GET` | `/users/{user_id}` | Get a specific user | `200 OK` |
| `PUT` | `/users/{user_id}` | Update a user | `200 OK` |
| `DELETE` | `/users/{user_id}` | Delete a user | `204 No Content` |
| `PATCH` | `/users/{user_id}/deactivate` | Deactivate a user | `200 OK` |

### 🗓️ Course Management

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| `POST` | `/courses/` | Create a new course | `201 Created` |
| `GET` | `/courses/` | Get all courses | `200 OK` |
| `GET` | `/courses/{course_id}` | Get a specific course | `200 OK` |
| `PUT` | `/courses/{course_id}` | Update a course | `200 OK` |
| `DELETE` | `/courses/{course_id}` | Delete a course | `204 No Content` |
| `PATCH` | `/courses/{course_id}/close` | Close enrollment for a course | `200 OK` |
| `GET` | `/courses/{course_id}/enrolled-users` | Get users enrolled in a course | `200 OK` |

### 📝 Enrollment Management

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| `POST` | `/enrollments/` | Enroll a user in a course | `201 Created` |
| `GET` | `/enrollments/` | Get all enrollments | `200 OK` |
| `GET` | `/enrollments/{enrollment_id}` | Get a specific enrollment | `200 OK` |
| `PUT` | `/enrollments/{enrollment_id}` | Update an enrollment | `200 OK` |
| `DELETE` | `/enrollments/{enrollment_id}` | Delete an enrollment | `204 No Content` |
| `PATCH` | `/enrollments/{enrollment_id}/complete` | Mark course as completed | `200 OK` |
| `GET` | `/enrollments/user/{user_id}` | Get enrollments for a user | `200 OK` |
| `GET` | `/enrollments/course/{course_id}` | Get enrollments for a course | `200 OK` |

### 🏠 System Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| `GET` | `/` | API welcome message and overview | `200 OK` |
| `GET` | `/health` | Health check endpoint | `200 OK` |

## 📊 Data Models

### 👤 User Model
```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "is_active": true,
  "created_at": "2025-01-16T10:00:00Z"
}
```

**Fields:**
- `id` (int): Unique identifier (auto-generated)
- `name` (str): Full name of the user
- `email` (str): Valid email address (unique)
- `is_active` (bool): Whether the user is active (default: true)
- `created_at` (datetime): Timestamp when user was created

### 🗓️ Course Model
```json
{
  "id": 1,
  "title": "Python Basics",
  "description": "Learn Python",
  "is_open": true,
  "created_at": "2025-01-16T10:00:00Z"
}
```

**Fields:**
- `id` (int): Unique identifier (auto-generated)
- `title` (str): Name of the course
- `description` (str): Brief description of the course
- `is_open` (bool): Whether the course is open for enrollment (default: true)
- `created_at` (datetime): Timestamp when course was created

### 📝 Enrollment Model
```json
{
  "id": 1,
  "user_id": 1,
  "course_id": 1,
  "enrolled_date": "2025-01-16",
  "completed": false,
  "created_at": "2025-01-16T10:00:00Z"
}
```

**Fields:**
- `id` (int): Unique identifier (auto-generated)
- `user_id` (int): ID of the enrolling user
- `course_id` (int): ID of the course
- `enrolled_date` (date): Date of enrollment (default: today)
- `completed` (bool): Whether the course was completed (default: false)
- `created_at` (datetime): Timestamp when enrollment was created

### 📋 Enrollment with Details Model
```json
{
  "id": 1,
  "user_id": 1,
  "course_id": 1,
  "enrolled_date": "2025-01-16",
  "completed": false,
  "created_at": "2025-01-16T10:00:00Z",
  "user_name": "Alice",
  "course_title": "Python Basics"
}
```

**Additional Fields:**
- `user_name` (str): Name of the enrolled user
- `course_title` (str): Title of the enrolled course

## 🔒 Business Rules & Validation

### 📝 **Enrollment Rules**
- ✅ **Active Users Only**: Only active users can enroll in courses
- ✅ **No Duplicate Enrollments**: Users cannot enroll in the same course twice
- ✅ **Open Courses Only**: Courses must be open for enrollment
- ✅ **Valid References**: Both user and course must exist

### 🛡️ **Data Integrity**
- ✅ **Protected Deletions**: Users with enrollments cannot be deleted
- ✅ **Protected Deletions**: Courses with enrollments cannot be deleted
- ✅ **Unique Emails**: Email addresses must be unique across all users
- ✅ **Referential Integrity**: All foreign key relationships are validated

### 🗓️ **Course Management**
- ✅ **Enrollment Control**: Closing enrollment prevents new enrollments
- ✅ **Existing Enrollments**: Existing enrollments remain valid when course is closed
- ✅ **Status Persistence**: Course status changes don't affect existing enrollments

### ⚠️ **Error Handling**
- ✅ **404 Not Found**: For non-existent resources
- ✅ **400 Bad Request**: For validation errors and business rule violations
- ✅ **201 Created**: For successful resource creation
- ✅ **204 No Content**: For successful deletions

## 🧪 Testing

### 🚀 **Run Tests**

**Run all tests:**
```bash
python -m pytest test_api.py -v
```

**Run specific test categories:**
```bash
# User tests only
python -m pytest test_api.py::TestUserEndpoints -v

# Course tests only  
python -m pytest test_api.py::TestCourseEndpoints -v

# Enrollment tests only
python -m pytest test_api.py::TestEnrollmentEndpoints -v

# System tests only
python -m pytest test_api.py::TestRootEndpoints -v
```

**Run with coverage:**
```bash
python -m pytest test_api.py --cov=. --cov-report=html
```

### 📊 **Test Coverage**

The comprehensive test suite includes **25+ test cases** covering:

| Test Category | Coverage |
|---------------|----------|
| **👤 User Operations** | ✅ Create, Read, Update, Delete, Deactivate |
| **🗓️ Course Operations** | ✅ Create, Read, Update, Delete, Close enrollment |
| **📝 Enrollment Operations** | ✅ Enroll, Complete, View, Update, Delete |
| **🔒 Business Rules** | ✅ All validation rules and constraints |
| **⚠️ Error Handling** | ✅ 404, 400, and edge case scenarios |
| **🛡️ Data Integrity** | ✅ Referential integrity and constraints |
| **🏠 System Endpoints** | ✅ Health check and root endpoints |

### 🎯 **Test Features**
- ✅ **Automatic Database Reset**: Each test starts with clean data
- ✅ **Example Data Validation**: Tests verify pre-loaded example data
- ✅ **Business Rule Testing**: All enrollment rules are tested
- ✅ **Error Scenario Testing**: Invalid requests and edge cases
- ✅ **Status Code Validation**: Proper HTTP response codes

## 🎯 Example Usage

### 👤 **User Management**

**Create a new user:**
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "is_active": true
  }'
```

**Get all users:**
```bash
curl -X GET "http://localhost:8000/users/"
```

**Deactivate a user:**
```bash
curl -X PATCH "http://localhost:8000/users/1/deactivate"
```

### 🗓️ **Course Management**

**Create a new course:**
```bash
curl -X POST "http://localhost:8000/courses/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Advanced Python",
    "description": "Learn advanced Python concepts",
    "is_open": true
  }'
```

**Get all courses:**
```bash
curl -X GET "http://localhost:8000/courses/"
```

**Close enrollment for a course:**
```bash
curl -X PATCH "http://localhost:8000/courses/1/close"
```

**Get users enrolled in a course:**
```bash
curl -X GET "http://localhost:8000/courses/1/enrolled-users"
```

### 📝 **Enrollment Management**

**Enroll a user in a course:**
```bash
curl -X POST "http://localhost:8000/enrollments/" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "course_id": 1
  }'
```

**Mark course as completed:**
```bash
curl -X PATCH "http://localhost:8000/enrollments/1/complete"
```

**Get enrollments for a user:**
```bash
curl -X GET "http://localhost:8000/enrollments/user/1"
```

**Get all enrollments:**
```bash
curl -X GET "http://localhost:8000/enrollments/"
```

### 🏠 **System Endpoints**

**Check API status:**
```bash
curl -X GET "http://localhost:8000/health"
```

**Get API information:**
```bash
curl -X GET "http://localhost:8000/"
```

## 🛠️ Development

### 🏗️ **Architecture**

The application follows a **clean, modular architecture**:

- **📋 Schemas Layer**: Pydantic models for data validation and serialization
- **🛣️ Routes Layer**: FastAPI route handlers for HTTP endpoints
- **⚙️ Services Layer**: Business logic and data operations
- **💾 Data Layer**: In-memory storage with automatic initialization

### 🛠️ **Tech Stack**

| Technology | Version | Purpose |
|------------|---------|---------|
| **FastAPI** | 0.116.1+ | Modern, fast web framework for building APIs |
| **Pydantic** | 2.11.7+ | Data validation using Python type annotations |
| **Uvicorn** | 0.35.0+ | ASGI server for running the application |
| **Pytest** | 8.4.2+ | Testing framework with comprehensive coverage |
| **Email-Validator** | 2.3.0+ | Email validation for user registration |

### 🔧 **Development Features**

- ✅ **Hot Reload**: Automatic server restart on code changes
- ✅ **Type Hints**: Full type annotation support
- ✅ **Auto Documentation**: Interactive API docs generated automatically
- ✅ **Validation**: Comprehensive request/response validation
- ✅ **Error Handling**: Proper HTTP status codes and error messages
- ✅ **Testing**: Comprehensive test suite with 25+ test cases

### 📁 **File Organization**

```
📁 Project Structure
├── 📄 main.py                    # 🚀 Application entry point
├── 📄 run_server.py              # 🎮 Development server script
├── 📄 test_api.py               # 🧪 Test suite
├── 📁 schemas/                  # 📋 Data models
│   ├── 📄 user.py              # 👤 User schemas
│   ├── 📄 course.py            # 🗓️ Course schemas
│   └── 📄 enrollment.py        # 📝 Enrollment schemas
├── 📁 routes/                   # 🛣️ API endpoints
│   ├── 📄 users.py             # 👤 User routes
│   ├── 📄 courses.py           # 🗓️ Course routes
│   └── 📄 enrollments.py       # 📝 Enrollment routes
└── 📁 services/                 # ⚙️ Business logic
    ├── 📄 database.py          # 💾 Data storage
    ├── 📄 user_service.py      # 👤 User operations
    ├── 📄 course_service.py    # 🗓️ Course operations
    └── 📄 enrollment_service.py # 📝 Enrollment operations
```

### 🚀 **Getting Started for Developers**

1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run tests**: `python -m pytest test_api.py -v`
4. **Start development server**: `python run_server.py`
5. **Access docs**: `http://localhost:8000/docs`

### 📝 **Contributing**

- Follow the existing code structure and patterns
- Add tests for any new functionality
- Ensure all tests pass before submitting changes
- Use type hints and proper documentation

## 📄 License

This project is created for **educational purposes** and demonstrates modern API development practices with FastAPI.

---

## 🎉 **Ready to Use!**

Your EduTrack Lite API is now ready with:
- ✅ **21 API endpoints** covering all requirements
- ✅ **Comprehensive testing** with 25+ test cases
- ✅ **Interactive documentation** at `/docs`
- ✅ **Example data** pre-loaded and ready
- ✅ **Business rules** fully implemented
- ✅ **Clean architecture** following best practices

**Start the server and explore the API at `http://localhost:8000/docs`!** 🚀
