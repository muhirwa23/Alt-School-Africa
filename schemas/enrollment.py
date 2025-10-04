from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class EnrollmentBase(BaseModel):
    user_id: int
    course_id: int
    enrolled_date: date
    completed: bool = False


class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int
    enrolled_date: Optional[date] = None


class EnrollmentUpdate(BaseModel):
    completed: Optional[bool] = None


class Enrollment(EnrollmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class EnrollmentWithDetails(Enrollment):
    user_name: str
    course_title: str
