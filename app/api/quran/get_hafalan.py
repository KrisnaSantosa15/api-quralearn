import sqlalchemy as sa
from fastapi import Depends
from typing import List

from app.api_models.base_response import BaseResponseModel
from app.api_models.hafalan_model import HafalanModel
from app.dependencies.authentication import Authentication
from app.dependencies.get_db_session import get_db_session
from app.models.hafalan import Hafalan

class GetHafalanResponseModel(BaseResponseModel):
    data: List[HafalanModel]  # Change the data type to a list of HafalanModel

async def get_hafalan(payload=Depends(Authentication()), session=Depends(get_db_session)):
    user_id = payload.get('uid', 0)
    # Use filter to get all rows with Hafalan.id_user == user_id
    hafalans = session.query(Hafalan).filter(Hafalan.id_user == user_id).all()
    
    # Construct a list of HafalanModel instances from the result
    hafalan_models = [HafalanModel(
        id=hafalan.id,
        judul=hafalan.judul,
        tanggal=hafalan.tanggal,
        durasi=hafalan.durasi,
        judul_kanan=hafalan.judul_kanan,
        id_user=hafalan.id_user
    ) for hafalan in hafalans]
    
    return GetHafalanResponseModel(data=hafalan_models)
