from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """회원가입용 스키마 - 프론트엔드 폼과 일치"""
    email: EmailStr
    username: str
    password: str
    birth_date: Optional[date] = None


class UserUpdate(BaseModel):
    """사용자 정보 수정용 스키마"""
    username: Optional[str] = None
    birth_date: Optional[date] = None


class UserResponse(BaseModel):
    """사용자 정보 응답용 스키마"""
    id: int
    email: str
    username: str
    birth_date: Optional[date] = None
    is_active: bool
    is_loco: bool
    created_at: datetime

    class Config:
        from_attributes = True


# 별칭 설정
User = UserResponse


class UserInDB(UserResponse):
    """데이터베이스용 스키마 (비밀번호 포함)"""
    hashed_password: str