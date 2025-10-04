from typing import List
from fastapi import APIRouter, status
from schemas.user import User, UserCreate, UserUpdate
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    """Create a new user"""
    return UserService.create_user(user_data)


@router.get("/", response_model=List[User])
async def get_all_users():
    """Get all users"""
    return UserService.get_all_users()


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Get a user by ID"""
    return UserService.get_user(user_id)


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_data: UserUpdate):
    """Update a user"""
    return UserService.update_user(user_id, user_data)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Delete a user"""
    UserService.delete_user(user_id)


@router.patch("/{user_id}/deactivate", response_model=User)
async def deactivate_user(user_id: int):
    """Deactivate a user"""
    return UserService.deactivate_user(user_id)
