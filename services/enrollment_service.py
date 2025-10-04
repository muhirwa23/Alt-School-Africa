from datetime import datetime, date
from typing import List, Optional
from fastapi import HTTPException, status
from schemas.enrollment import Enrollment, EnrollmentCreate, EnrollmentUpdate, EnrollmentWithDetails
from services.database import db
from services.user_service import UserService
from services.course_service import CourseService


class EnrollmentService:
    @staticmethod
    def enroll_user(enrollment_data: EnrollmentCreate) -> Enrollment:
        """Enroll a user in a course"""
        # Validate user exists and is active
        if not UserService.is_user_active(enrollment_data.user_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found or not active"
            )
        
        # Validate course exists and is open
        if not CourseService.is_course_open(enrollment_data.course_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Course not found or not open for enrollment"
            )
        
        # Check if user is already enrolled in this course
        for enrollment in db.enrollments.values():
            if (enrollment.user_id == enrollment_data.user_id and 
                enrollment.course_id == enrollment_data.course_id):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User is already enrolled in this course"
                )
        
        enrollment_id = db.get_next_enrollment_id()
        enrolled_date = enrollment_data.enrolled_date or date.today()
        
        enrollment = Enrollment(
            id=enrollment_id,
            user_id=enrollment_data.user_id,
            course_id=enrollment_data.course_id,
            enrolled_date=enrolled_date,
            completed=False,
            created_at=datetime.now()
        )
        
        db.enrollments[enrollment_id] = enrollment
        db.increment_enrollment_counter()
        return enrollment
    
    @staticmethod
    def get_enrollment(enrollment_id: int) -> Enrollment:
        """Get an enrollment by ID"""
        if enrollment_id not in db.enrollments:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"
            )
        return db.enrollments[enrollment_id]
    
    @staticmethod
    def get_all_enrollments() -> List[Enrollment]:
        """Get all enrollments"""
        return list(db.enrollments.values())
    
    @staticmethod
    def get_user_enrollments(user_id: int) -> List[EnrollmentWithDetails]:
        """Get all enrollments for a specific user"""
        if user_id not in db.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        user_enrollments = []
        for enrollment in db.enrollments.values():
            if enrollment.user_id == user_id:
                # Get user and course details
                user = db.users[enrollment.user_id]
                course = db.courses[enrollment.course_id]
                
                enrollment_with_details = EnrollmentWithDetails(
                    id=enrollment.id,
                    user_id=enrollment.user_id,
                    course_id=enrollment.course_id,
                    enrolled_date=enrollment.enrolled_date,
                    completed=enrollment.completed,
                    created_at=enrollment.created_at,
                    user_name=user.name,
                    course_title=course.title
                )
                user_enrollments.append(enrollment_with_details)
        
        return user_enrollments
    
    @staticmethod
    def get_course_enrollments(course_id: int) -> List[EnrollmentWithDetails]:
        """Get all enrollments for a specific course"""
        if course_id not in db.courses:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Course not found"
            )
        
        course_enrollments = []
        for enrollment in db.enrollments.values():
            if enrollment.course_id == course_id:
                # Get user and course details
                user = db.users[enrollment.user_id]
                course = db.courses[enrollment.course_id]
                
                enrollment_with_details = EnrollmentWithDetails(
                    id=enrollment.id,
                    user_id=enrollment.user_id,
                    course_id=enrollment.course_id,
                    enrolled_date=enrollment.enrolled_date,
                    completed=enrollment.completed,
                    created_at=enrollment.created_at,
                    user_name=user.name,
                    course_title=course.title
                )
                course_enrollments.append(enrollment_with_details)
        
        return course_enrollments
    
    @staticmethod
    def mark_completion(enrollment_id: int, completed: bool = True) -> Enrollment:
        """Mark a course as completed or not completed"""
        if enrollment_id not in db.enrollments:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"
            )
        
        enrollment = db.enrollments[enrollment_id]
        enrollment.completed = completed
        return enrollment
    
    @staticmethod
    def update_enrollment(enrollment_id: int, enrollment_data: EnrollmentUpdate) -> Enrollment:
        """Update an enrollment"""
        if enrollment_id not in db.enrollments:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"
            )
        
        enrollment = db.enrollments[enrollment_id]
        
        if enrollment_data.completed is not None:
            enrollment.completed = enrollment_data.completed
        
        return enrollment
    
    @staticmethod
    def delete_enrollment(enrollment_id: int) -> None:
        """Delete an enrollment"""
        if enrollment_id not in db.enrollments:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Enrollment not found"
            )
        
        del db.enrollments[enrollment_id]
