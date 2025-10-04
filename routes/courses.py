from typing import List
from fastapi import APIRouter, status
from schemas.course import Course, CourseCreate, CourseUpdate
from schemas.user import User
from services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_course(course_data: CourseCreate):
    """Create a new course"""
    return CourseService.create_course(course_data)


@router.get("/", response_model=List[Course])
async def get_all_courses():
    """Get all courses"""
    return CourseService.get_all_courses()


@router.get("/{course_id}", response_model=Course)
async def get_course(course_id: int):
    """Get a course by ID"""
    return CourseService.get_course(course_id)


@router.put("/{course_id}", response_model=Course)
async def update_course(course_id: int, course_data: CourseUpdate):
    """Update a course"""
    return CourseService.update_course(course_id, course_data)


@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    """Delete a course"""
    CourseService.delete_course(course_id)


@router.patch("/{course_id}/close", response_model=Course)
async def close_enrollment(course_id: int):
    """Close enrollment for a course"""
    return CourseService.close_enrollment(course_id)


@router.get("/{course_id}/enrolled-users", response_model=List[User])
async def get_enrolled_users(course_id: int):
    """Get all users enrolled in a particular course"""
    return CourseService.get_enrolled_users(course_id)
