from fastapi import APIRouter
from app.api.v1.endpoints import auth, users

api_router = APIRouter()

# 인증과 사용자 관리만 우선 등록
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])