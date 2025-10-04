import pytest
from fastapi.testclient import TestClient
from main import app
from services.database import db

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_database():
    """Reset database before each test"""
    # Clear all data
    db.users.clear()
    db.courses.clear()
    db.enrollments.clear()
    
    # Reset counters
    db._user_counter = 1
    db._course_counter = 1
    db._enrollment_counter = 1
    
    # Reinitialize example data
    db._initialize_example_data()


class TestUserEndpoints:
    def test_create_user(self):
        """Test creating a new user"""
        user_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "is_active": True
        }
        response = client.post("/users/", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John Doe"
        assert data["email"] == "john@example.com"
        assert data["is_active"] is True
        assert "id" in data
        assert "created_at" in data

    def test_create_user_duplicate_email(self):
        """Test creating user with duplicate email"""
        user_data = {
            "name": "Alice Smith",
            "email": "alice@example.com",  # This email already exists in example data
            "is_active": True
        }
        response = client.post("/users/", json=user_data)
        assert response.status_code == 400
        assert "Email already exists" in response.json()["detail"]

    def test_get_all_users(self):
        """Test getting all users"""
        response = client.get("/users/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1  # Only the example user
        assert data[0]["name"] == "Alice"

    def test_get_user(self):
        """Test getting a specific user"""
        response = client.get("/users/1")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Alice"
        assert data["email"] == "alice@example.com"

    def test_get_user_not_found(self):
        """Test getting a non-existent user"""
        response = client.get("/users/999")
        assert response.status_code == 404
        assert "User not found" in response.json()["detail"]

    def test_update_user(self):
        """Test updating a user"""
        update_data = {
            "name": "Alice Updated",
            "is_active": False
        }
        response = client.put("/users/1", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Alice Updated"
        assert data["is_active"] is False
        assert data["email"] == "alice@example.com"  # Should remain unchanged

    def test_deactivate_user(self):
        """Test deactivating a user"""
        response = client.patch("/users/1/deactivate")
        assert response.status_code == 200
        data = response.json()
        assert data["is_active"] is False

    def test_delete_user(self):
        """Test deleting a user"""
        response = client.delete("/users/1")
        assert response.status_code == 204

    def test_delete_user_with_enrollments(self):
        """Test deleting a user with enrollments should fail"""
        response = client.delete("/users/1")
        assert response.status_code == 400
        assert "Cannot delete user with existing enrollments" in response.json()["detail"]


class TestCourseEndpoints:
    def test_create_course(self):
        """Test creating a new course"""
        course_data = {
            "title": "Advanced Python",
            "description": "Learn advanced Python concepts",
            "is_open": True
        }
        response = client.post("/courses/", json=course_data)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Advanced Python"
        assert data["description"] == "Learn advanced Python concepts"
        assert data["is_open"] is True
        assert "id" in data
        assert "created_at" in data

    def test_get_all_courses(self):
        """Test getting all courses"""
        response = client.get("/courses/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1  # Only the example course
        assert data[0]["title"] == "Python Basics"

    def test_get_course(self):
        """Test getting a specific course"""
        response = client.get("/courses/1")
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Python Basics"
        assert data["description"] == "Learn Python"

    def test_get_course_not_found(self):
        """Test getting a non-existent course"""
        response = client.get("/courses/999")
        assert response.status_code == 404
        assert "Course not found" in response.json()["detail"]

    def test_update_course(self):
        """Test updating a course"""
        update_data = {
            "title": "Python Basics Updated",
            "is_open": False
        }
        response = client.put("/courses/1", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Python Basics Updated"
        assert data["is_open"] is False
        assert data["description"] == "Learn Python"  # Should remain unchanged

    def test_close_enrollment(self):
        """Test closing enrollment for a course"""
        response = client.patch("/courses/1/close")
        assert response.status_code == 200
        data = response.json()
        assert data["is_open"] is False

    def test_get_enrolled_users(self):
        """Test getting enrolled users for a course"""
        response = client.get("/courses/1/enrolled-users")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1  # Alice is enrolled
        assert data[0]["name"] == "Alice"

    def test_delete_course(self):
        """Test deleting a course"""
        # First create a course without enrollments
        course_data = {
            "title": "Test Course",
            "description": "Test Description",
            "is_open": True
        }
        response = client.post("/courses/", json=course_data)
        course_id = response.json()["id"]
        
        response = client.delete(f"/courses/{course_id}")
        assert response.status_code == 204

    def test_delete_course_with_enrollments(self):
        """Test deleting a course with enrollments should fail"""
        response = client.delete("/courses/1")
        assert response.status_code == 400
        assert "Cannot delete course with existing enrollments" in response.json()["detail"]


class TestEnrollmentEndpoints:
    def test_enroll_user(self):
        """Test enrolling a user in a course"""
        # First create a new user and course
        user_data = {
            "name": "Bob Smith",
            "email": "bob@example.com",
            "is_active": True
        }
        user_response = client.post("/users/", json=user_data)
        user_id = user_response.json()["id"]
        
        course_data = {
            "title": "JavaScript Basics",
            "description": "Learn JavaScript",
            "is_open": True
        }
        course_response = client.post("/courses/", json=course_data)
        course_id = course_response.json()["id"]
        
        enrollment_data = {
            "user_id": user_id,
            "course_id": course_id
        }
        response = client.post("/enrollments/", json=enrollment_data)
        assert response.status_code == 201
        data = response.json()
        assert data["user_id"] == user_id
        assert data["course_id"] == course_id
        assert data["completed"] is False
        assert "enrolled_date" in data

    def test_enroll_inactive_user(self):
        """Test enrolling an inactive user should fail"""
        # Deactivate the example user
        client.patch("/users/1/deactivate")
        
        enrollment_data = {
            "user_id": 1,
            "course_id": 1
        }
        response = client.post("/enrollments/", json=enrollment_data)
        assert response.status_code == 400
        assert "User not found or not active" in response.json()["detail"]

    def test_enroll_in_closed_course(self):
        """Test enrolling in a closed course should fail"""
        # Close the example course
        client.patch("/courses/1/close")
        
        # Create a new active user
        user_data = {
            "name": "Bob Smith",
            "email": "bob@example.com",
            "is_active": True
        }
        user_response = client.post("/users/", json=user_data)
        user_id = user_response.json()["id"]
        
        enrollment_data = {
            "user_id": user_id,
            "course_id": 1
        }
        response = client.post("/enrollments/", json=enrollment_data)
        assert response.status_code == 400
        assert "Course not found or not open for enrollment" in response.json()["detail"]

    def test_duplicate_enrollment(self):
        """Test enrolling the same user twice in the same course should fail"""
        enrollment_data = {
            "user_id": 1,
            "course_id": 1
        }
        response = client.post("/enrollments/", json=enrollment_data)
        assert response.status_code == 400
        assert "User is already enrolled in this course" in response.json()["detail"]

    def test_get_all_enrollments(self):
        """Test getting all enrollments"""
        response = client.get("/enrollments/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1  # Only the example enrollment
        assert data[0]["user_id"] == 1
        assert data[0]["course_id"] == 1

    def test_get_enrollment(self):
        """Test getting a specific enrollment"""
        response = client.get("/enrollments/1")
        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == 1
        assert data["course_id"] == 1
        assert data["completed"] is False

    def test_mark_completion(self):
        """Test marking a course as completed"""
        response = client.patch("/enrollments/1/complete")
        assert response.status_code == 200
        data = response.json()
        assert data["completed"] is True

    def test_get_user_enrollments(self):
        """Test getting enrollments for a specific user"""
        response = client.get("/enrollments/user/1")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["user_id"] == 1
        assert data[0]["user_name"] == "Alice"
        assert data[0]["course_title"] == "Python Basics"

    def test_get_course_enrollments(self):
        """Test getting enrollments for a specific course"""
        response = client.get("/enrollments/course/1")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["course_id"] == 1
        assert data[0]["user_name"] == "Alice"
        assert data[0]["course_title"] == "Python Basics"

    def test_update_enrollment(self):
        """Test updating an enrollment"""
        update_data = {
            "completed": True
        }
        response = client.put("/enrollments/1", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["completed"] is True

    def test_delete_enrollment(self):
        """Test deleting an enrollment"""
        response = client.delete("/enrollments/1")
        assert response.status_code == 204


class TestRootEndpoints:
    def test_root_endpoint(self):
        """Test the root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "endpoints" in data

    def test_health_check(self):
        """Test the health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
