from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title="Travel Platform API",
    description="한국 여행 서비스 플랫폼 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Travel Platform API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}