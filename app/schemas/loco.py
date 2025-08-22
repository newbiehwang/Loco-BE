from typing import Optional, List
from pydantic import BaseModel


class LocoCreate(BaseModel):
    """로코 프로필 생성용 스키마"""
    introduction: Optional[str] = None
    specialties: Optional[str] = None
    languages: Optional[str] = None
    hourly_rate: Optional[int] = None
    region_id: int


class LocoUpdate(BaseModel):
    """로코 프로필 수정용 스키마"""
    introduction: Optional[str] = None
    specialties: Optional[str] = None
    languages: Optional[str] = None
    hourly_rate: Optional[int] = None
    is_available: Optional[bool] = None


class LocoResponse(BaseModel):
    """로코 프로필 응답용 스키마"""
    id: int
    user_id: int
    introduction: Optional[str]
    specialties: Optional[str]
    languages: Optional[str]
    hourly_rate: Optional[int]
    region_id: int
    rating: float
    total_reviews: int
    is_verified: bool
    is_available: bool

    class Config:
        from_attributes = True


# 별칭 설정
Loco = LocoResponse