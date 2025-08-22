from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.services.auth_service import auth_service
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import Token

router = APIRouter()


@router.post("/register", response_model=UserResponse, summary="회원가입")
def register(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreate,
):
    """
    새 사용자 회원가입

    - **email**: 이메일 주소 (로그인 ID로 사용)
    - **username**: 사용자명/닉네임
    - **password**: 비밀번호
    - **birth_date**: 생년월일 (선택사항)
    """
    user = auth_service.register_user(db, user_data=user_in)
    return user


@router.post("/login", response_model=Token, summary="로그인")
def login(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    사용자 로그인

    - **username**: 이메일 주소
    - **password**: 비밀번호

    성공시 JWT 토큰 반환
    """
    user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = auth_service.create_access_token_for_user(user)
    return token_data