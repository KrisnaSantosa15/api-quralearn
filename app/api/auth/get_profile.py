import sqlalchemy as sa
from fastapi import Depends

from app.api_models.base_response import BaseResponseModel
from app.api_models.profile_model import ProfileModel
from app.dependencies.authentication import Authentication
from app.dependencies.get_db_session import get_db_session
from app.models.user import User


class GetProfileResponseModel(BaseResponseModel):
    data: ProfileModel

    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'id': 1000,
                    'username': 'shinhayata',
                    'full_name': 'Shin Hayata'
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def get_profile(payload = Depends(Authentication()), session = Depends(get_db_session)):
    user_id = payload.get('uid', 0)
    profile = session.execute(
        sa.select(
            User.id,
            User.username,
            User.full_name
        ).where(
            User.id == user_id
        )
    ).fetchone()

    return GetProfileResponseModel(
        data=ProfileModel(
            id=profile.id,
            username=profile.username,
            full_name=profile.full_name
        )
    )