from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_active_user
from app.crud.user import crud_user
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate

router = APIRouter()

@router.get("/me", response_model=UserResponse, summary="내 정보 조회")
def read_user_me(
    current_user: User = Depends(get_current_active_user),
):
    """현재 로그인한 사용자의 정보 조회"""
    return current_user

@router.put("/me", response_model=UserResponse, summary="내 정보 수정")
def update_user_me(
    *,
    db: Session = Depends(get_db),
    user_in: UserUpdate,
    current_user: User = Depends(get_current_active_user),
):
    """현재 로그인한 사용자의 정보 수정"""
    user = crud_user.update(db, db_obj=current_user, obj_in=user_in)
    return user

@router.get("/{user_id}", response_model=UserResponse, summary="사용자 정보 조회")
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """특정 사용자 정보 조회 (공개 정보만)"""
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user