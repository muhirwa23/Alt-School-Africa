from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException, status
from schemas.course import Course, CourseCreate, CourseUpdate
from schemas.user import User
from services.database import db


class CourseService:
    @staticmethod
    def create_course(course_data: CourseCreate) -> Course:
        """Create a new course"""
        course_id = db.get_next_course_id()
        course = Course(
            id=course_id,
            title=course_data.title,
            description=course_data.description,
            is_open=course_data.is_open,
            created_at=datetime.now()
        )
        
        db.courses[course_id] = course
        db.increment_course_counter()
        return course
    
    @staticmethod
    def get_course(course_id: int) -> Course:
        """Get a course by ID"""
        if course_id not in db.courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        return db.courses[course_id]
    
    @staticmethod
    def get_all_courses() -> List[Course]:
        """Get all courses"""
        return list(db.courses.values())
    
    @staticmethod
    def update_course(course_id: int, course_data: CourseUpdate) -> Course:
        """Update a course"""
        if course_id not in db.courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        
        course = db.courses[course_id]
        
        # Update fields
        if course_data.title is not None:
            course.title = course_data.title
        if course_data.description is not None:
            course.description = course_data.description
        if course_data.is_open is not None:
            course.is_open = course_data.is_open
        
        return course
    
    @staticmethod
    def delete_course(course_id: int) -> None:
        """Delete a course"""
        if course_id not in db.courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        
        # Check if course has any enrollments
        for enrollment in db.enrollments.values():
            if enrollment.course_id == course_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Cannot delete course with existing enrollments"
                )
        
        del db.courses[course_id]
    
    @staticmethod
    def close_enrollment(course_id: int) -> Course:
        """Close enrollment for a course"""
        if course_id not in db.courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        
        course = db.courses[course_id]
        course.is_open = False
        return course
    
    @staticmethod
    def get_enrolled_users(course_id: int) -> List[User]:
        """Get all users enrolled in a particular course"""
        if course_id not in db.courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        
        enrolled_user_ids = set()
        for enrollment in db.enrollments.values():
            if enrollment.course_id == course_id:
                enrolled_user_ids.add(enrollment.user_id)
        
        enrolled_users = []
        for user_id in enrolled_user_ids:
            if user_id in db.users:
                enrolled_users.append(db.users[user_id])
        
        return enrolled_users
    
    @staticmethod
    def is_course_open(course_id: int) -> bool:
        """Check if a course is open for enrollment"""
        if course_id not in db.courses:
            return False
        return db.courses[course_id].is_open
