from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_active_user
from app.crud.loco import crud_loco
from app.services.loco_service import LocoService
from app.models.user import User
from app.schemas.loco import Loco, LocoCreate, LocoUpdate

router = APIRouter()

@router.get("/", response_model=List[Loco])
def read_locos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """로코 목록 조회"""
    locos = crud_loco.get_multi(db, skip=skip, limit=limit)
    return locos

@router.post("/", response_model=Loco)
def create_loco_profile(
    *,
    db: Session = Depends(get_db),
    loco_in: LocoCreate,
    current_user: User = Depends(get_current_active_user),
):
    """로코 프로필 생성"""
    loco = LocoService.create_loco_profile(db, loco_data=loco_in, user=current_user)
    return loco

@router.get("/region/{region_id}", response_model=List[Loco])
def read_locos_by_region(
    region_id: int,
    db: Session = Depends(get_db)
):
    """지역별 로코 조회"""
    locos = crud_loco.get_by_region(db, region_id=region_id)
    return locos