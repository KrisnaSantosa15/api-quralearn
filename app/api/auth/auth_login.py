import time
import sqlalchemy as sa
from pydantic import BaseModel
from fastapi import Depends
from fastapi.exceptions import HTTPException
from werkzeug.security import check_password_hash

from app.api_models.base_response import BaseResponseModel
from app.models.user import User
from app.models.user_login import UserLogin
from app.dependencies.get_db_session import get_db_session
from app.config import config
from app.utils.generate_refresh_token import generate_refresh_token
from app.utils.generate_access_token import generate_access_token

class LoginData(BaseModel):
    username: str
    password: str

class LoginDataResponseModel(BaseModel):
    user_id: int
    username: str
    refresh_token: str
    access_token: str
    expired_at: int
    
class LoginResponseModel(BaseResponseModel):
    data: LoginDataResponseModel
    
    class Config:
        json_schema_extra = {
            "example": {
                "data": {
                    "user_id": 1000,
                    "username": "krisna",
                    "refresh_token": "abc.def.ghi",
                    "access_token": "jkl.mno.pqr",
                    "expired_at": 1630000000
                },
                "meta": {},
                "success": True,
                "code": 200,
                "message": "Success"
            }
        }

async def auth_login(data: LoginData, session = Depends(get_db_session)):
    #check username is valid
    user = session.execute(
        sa.select(
            User.id,
            User.password
        ).where(User.username == data.username)
    ).fetchone()
    
    if not user or not check_password_hash(user.password, data.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    payload = {
        "uid": user.id,
        "username": data.username,
        
    }
    refresh_token = generate_refresh_token(payload)
    
    user_login = UserLogin(
        user_id=user.id,
        refresh_token= refresh_token,
        expired_at=sa.func.TIMESTAMPADD(
            sa.text('SECOND'),
            config.REFRESH_TOKEN_EXPIRATION,
            sa.func.NOW()
        )
    )
    
    session.add(user_login)
    session.commit()
    
    access_token,access_token_expired_at = generate_access_token(payload)
    
    return LoginResponseModel(
        data=LoginDataResponseModel(
            user_id=user.id,
            username=data.username,
            refresh_token=refresh_token,
            access_token=access_token,
            expired_at=access_token_expired_at
        )
    )