from typing import Optional
import sqlalchemy as sa
from pydantic import BaseModel, model_validator
from fastapi import Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash

from app.dependencies.authentication import Authentication
from app.dependencies.get_db_session import get_db_session
from app.models.user import User


class EditProfileData(BaseModel):
    username: Optional[str]
    full_name: Optional[str]
    password: Optional[str]
    confirm_password: Optional[str]

    @model_validator(mode='after')
    def validate_confirm_password(self) -> 'EditProfileData':
        password = self.password
        confirm_password = self.confirm_password

        if password and confirm_password != password:
            raise ValueError('Confirm password does not match')

        return self

async def edit_profile(data: EditProfileData, payload = Depends(Authentication()), session = Depends(get_db_session)):
    profile_data = jsonable_encoder(data)

    user_id = payload.get('uid', 0)

    values_to_update = {}

    if 'username' in profile_data and profile_data['username']:
        # check username exist
        check_username = session.execute(
            sa.select(User.id).where(
                sa.and_(
                    User.username == profile_data['username'],
                    User.id != user_id
                )
            )
        ).fetchone()

        if check_username:
            raise HTTPException(400, 'Username already used')
        
        values_to_update.update({'username': profile_data['username']})
    
    if 'full_name' in profile_data and profile_data['full_name']:
        values_to_update.update({'full_name': profile_data['full_name']})
    
    if 'password' in profile_data and profile_data['password']:
        password = generate_password_hash(profile_data['password'])
        values_to_update.update({'password': password})

    result = session.execute(
        sa.update(
            User
        ).values(
            **values_to_update
        ).where(
            User.id == user_id
        )
    )

    if result.rowcount == 0:
        raise HTTPException(400, detail='User not found')


    session.commit()
    return Response(status_code=204)