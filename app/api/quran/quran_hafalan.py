import sqlalchemy as sa
from fastapi import Depends, Response, status
from pydantic import BaseModel

from app.dependencies.authentication import Authentication

from app.dependencies.get_db_session import get_db_session
from app.models.hafalan import Hafalan

class HafalanData(BaseModel):
    judul: str
    durasi: str
    judul_kanan: str

async def quran_hafalan(data: HafalanData, payload = Depends(Authentication()), session = Depends(get_db_session)):
    user_id = payload.get('uid', 0)
    
    hafalan = Hafalan(
            id_user=user_id,
            judul=data.judul, 
            durasi=data.durasi, 
            judul_kanan=data.judul_kanan
        )
    session.add(hafalan)
    session.commit()
    
    return Response(status_code=status.HTTP_201_CREATED)