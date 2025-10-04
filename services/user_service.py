from datetime import datetime
from typing import List, Optional
from fastapi import HTTPException, status
from schemas.user import User, UserCreate, UserUpdate
from services.database import db


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate) -> User:
        """Create a new user"""
        # Check if email already exists
        for existing_user in db.users.values():
            if existing_user.email == user_data.email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists"
                )
        
        user_id = db.get_next_user_id()
        user = User(
            id=user_id,
            name=user_data.name,
            email=user_data.email,
            is_active=user_data.is_active,
            created_at=datetime.now()
        )
        
        db.users[user_id] = user
        db.increment_user_counter()
        return user
    
    @staticmethod
    def get_user(user_id: int) -> User:
        """Get a user by ID"""
        if user_id not in db.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return db.users[user_id]
    
    @staticmethod
    def get_all_users() -> List[User]:
        """Get all users"""
        return list(db.users.values())
    
    @staticmethod
    def update_user(user_id: int, user_data: UserUpdate) -> User:
        """Update a user"""
        if user_id not in db.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        user = db.users[user_id]
        
        # Check if email is being updated and if it already exists
        if user_data.email and user_data.email != user.email:
            for existing_user in db.users.values():
                if existing_user.id != user_id and existing_user.email == user_data.email:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Email already exists"
                    )
        
        # Update fields
        if user_data.name is not None:
            user.name = user_data.name
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.is_active is not None:
            user.is_active = user_data.is_active
        
        return user
    
    @staticmethod
    def delete_user(user_id: int) -> None:
        """Delete a user"""
        if user_id not in db.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Check if user has any enrollments
        for enrollment in db.enrollments.values():
            if enrollment.user_id == user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Cannot delete user with existing enrollments"
                )
        
        del db.users[user_id]
    
    @staticmethod
    def deactivate_user(user_id: int) -> User:
        """Deactivate a user"""
        if user_id not in db.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        user = db.users[user_id]
        user.is_active = False
        return user
    
    @staticmethod
    def is_user_active(user_id: int) -> bool:
        """Check if a user is active"""
        if user_id not in db.users:
            return False
        return db.users[user_id].is_active
