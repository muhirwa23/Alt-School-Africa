from typing import List
from fastapi import APIRouter, status
from schemas.enrollment import Enrollment, EnrollmentCreate, EnrollmentUpdate, EnrollmentWithDetails
from services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/enrollments", tags=["enrollments"])


@router.post("/", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
async def enroll_user(enrollment_data: EnrollmentCreate):
    """Enroll a user in a course"""
    return EnrollmentService.enroll_user(enrollment_data)


@router.get("/", response_model=List[Enrollment])
async def get_all_enrollments():
    """Get all enrollments"""
    return EnrollmentService.get_all_enrollments()


@router.get("/{enrollment_id}", response_model=Enrollment)
async def get_enrollment(enrollment_id: int):
    """Get an enrollment by ID"""
    return EnrollmentService.get_enrollment(enrollment_id)


@router.put("/{enrollment_id}", response_model=Enrollment)
async def update_enrollment(enrollment_id: int, enrollment_data: EnrollmentUpdate):
    """Update an enrollment"""
    return EnrollmentService.update_enrollment(enrollment_id, enrollment_data)


@router.delete("/{enrollment_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_enrollment(enrollment_id: int):
    """Delete an enrollment"""
    EnrollmentService.delete_enrollment(enrollment_id)


@router.patch("/{enrollment_id}/complete", response_model=Enrollment)
async def mark_completion(enrollment_id: int, completed: bool = True):
    """Mark a course as completed"""
    return EnrollmentService.mark_completion(enrollment_id, completed)


@router.get("/user/{user_id}", response_model=List[EnrollmentWithDetails])
async def get_user_enrollments(user_id: int):
    """Get all enrollments for a specific user"""
    return EnrollmentService.get_user_enrollments(user_id)


@router.get("/course/{course_id}", response_model=List[EnrollmentWithDetails])
async def get_course_enrollments(course_id: int):
    """Get all enrollments for a specific course"""
    return EnrollmentService.get_course_enrollments(course_id)
