# app/crud/user.py
from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional

def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def get_by_nickname(db: Session, nickname: str) -> Optional[User]:
    return db.query(User).filter(User.nickname == nickname).first()

def create(db: Session, user_in: UserCreate, hashed_pw: str) -> User:
    user = User(
        email=user_in.email,
        hashed_password=hashed_pw,
        nickname=user_in.nickname,
        intro=user_in.intro,
        city_id=user_in.city_id,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update(db: Session, user: User, user_in: UserUpdate) -> User:
    if user_in.nickname is not None:
        user.nickname = user_in.nickname
    if user_in.intro is not None:
        user.intro = user_in.intro
    if user_in.city_id is not None:
        user.city_id = user_in.city_id
    db.commit()
    db.refresh(user)
    return user