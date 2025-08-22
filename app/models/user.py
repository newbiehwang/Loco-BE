# app/models/user.py
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    is_loco = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    trips = relationship(
        "Trip",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    loco_profile = relationship(
        "Loco",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )