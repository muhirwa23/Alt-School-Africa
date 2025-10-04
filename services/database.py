from datetime import datetime
from typing import Dict, List, Optional
from schemas.user import User
from schemas.course import Course
from schemas.enrollment import Enrollment


class Database:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.courses: Dict[int, Course] = {}
        self.enrollments: Dict[int, Enrollment] = {}
        self._user_counter = 1
        self._course_counter = 1
        self._enrollment_counter = 1
        
        # Initialize with example data
        self._initialize_example_data()
    
    def _initialize_example_data(self):
        """Initialize with the example data provided in requirements"""
        # Create example user
        user = User(
            id=self._user_counter,
            name="Alice",
            email="alice@example.com",
            is_active=True,
            created_at=datetime.now()
        )
        self.users[self._user_counter] = user
        self._user_counter += 1
        
        # Create example course
        course = Course(
            id=self._course_counter,
            title="Python Basics",
            description="Learn Python",
            is_open=True,
            created_at=datetime.now()
        )
        self.courses[self._course_counter] = course
        self._course_counter += 1
        
        # Create example enrollment
        enrollment = Enrollment(
            id=self._enrollment_counter,
            user_id=1,
            course_id=1,
            enrolled_date=datetime.now().date(),
            completed=False,
            created_at=datetime.now()
        )
        self.enrollments[self._enrollment_counter] = enrollment
        self._enrollment_counter += 1
    
    def get_next_user_id(self) -> int:
        """Get the next available user ID"""
        return self._user_counter
    
    def get_next_course_id(self) -> int:
        """Get the next available course ID"""
        return self._course_counter
    
    def get_next_enrollment_id(self) -> int:
        """Get the next available enrollment ID"""
        return self._enrollment_counter
    
    def increment_user_counter(self):
        """Increment the user counter"""
        self._user_counter += 1
    
    def increment_course_counter(self):
        """Increment the course counter"""
        self._course_counter += 1
    
    def increment_enrollment_counter(self):
        """Increment the enrollment counter"""
        self._enrollment_counter += 1


# Global database instance
db = Database()
