from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    user: dict

class TokenData(BaseModel):
    user_id: Optional[str] = None

class LoginRequest(BaseModel):
    username: str  # 이메일 주소
    password: str