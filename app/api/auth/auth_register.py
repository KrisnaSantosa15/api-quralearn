import sqlalchemy as sa
from fastapi import Response, status, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, model_validator
from app.dependencies.get_db_session import get_db_session
from app.models.user import User
from werkzeug.security import generate_password_hash

class RegisterData(BaseModel):
    username: str
    full_name: str
    password: str
    confirm_password: str
    
    @model_validator(mode='after')
    def check_passwords_match(self) -> 'RegisterData':
        pw1 = self.password
        pw2 = self.confirm_password
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self

async def auth_register(data: RegisterData, session = Depends(get_db_session)):
    #check if username is already taken
    check_username = session.execute(sa.select(User.id).where(User.username == data.username)).scalar_one_or_none()
    
    if check_username:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='username already taken')
    
    encrypted_password = generate_password_hash(data.password)
    
    user = User(username=data.username, full_name=data.full_name, password=encrypted_password)
    session.add(user)
    
    return Response(status_code=status.HTTP_201_CREATED)