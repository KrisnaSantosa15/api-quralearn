import sqlalchemy as sa
from fastapi import Depends, Response, status
from pydantic import BaseModel

from app.dependencies.authentication import Authentication
from app.dependencies.get_db_session import get_db_session

from app.models.kuis import Kuis

class KuisData(BaseModel):
    judul: str
    kecepatan: str
    ketepatan: str
    tipe: str

async def quran_kuis(data: KuisData, payload = Depends(Authentication()), session = Depends(get_db_session)):
    user_id = payload.get('uid', 0)
    
    kuis = Kuis(
        id_user = user_id,
        judul = data.judul,
        kecepatan = data.kecepatan,
        ketepatan = data.ketepatan,
        tipe = data.tipe
    )
    session.add(kuis)
    session.commit()
    
    return Response(status_code=status.HTTP_201_CREATED)