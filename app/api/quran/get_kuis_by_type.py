import sqlalchemy as sa
from pydantic import BaseModel
from fastapi import Depends
from typing import List

from app.api_models.base_response import BaseResponseModel
from app.api_models.kuis_model import KuisModel
from app.dependencies.authentication import Authentication
from app.dependencies.get_db_session import get_db_session
from app.models.kuis import Kuis

class GetKuisByTypeResponseModel(BaseModel):
    data: List[KuisModel]

async def get_kuis_by_type(type: str, payload=Depends(Authentication()), session=Depends(get_db_session)):
    """Get Kuis By Type
        
        This API is used to get kuis by type, the type is either 'TEBAK_SURAH' or 'SAMBUNG_AYAT'.
        if the type is not valid then return error.
    """
    user_id = payload.get('uid', 0)
    # if type is not 'TEBAK_SURAH' or 'SAMBUNG_AYAT' then return error
    if type != 'TEBAK_SURAH' and type != 'SAMBUNG_AYAT':
        return BaseResponseModel(code=400, message='type is not valid')
    
    # select * from kuis where id_user = user_id and tipe = type
    kuis_data = session.query(Kuis).filter(sa.and_(Kuis.id_user == user_id, Kuis.tipe == type)).all()
    # kuis_data = session.query(Kuis).filter(Kuis.id_user == user_id).all()
    
    kuis_models = [KuisModel(
        id=kuis.id,
        id_user=kuis.id_user,
        judul=kuis.judul,
        kecepatan=kuis.kecepatan,
        ketepatan=kuis.ketepatan,
        tanggal=kuis.tanggal,
        tipe=kuis.tipe
    ) for kuis in kuis_data]
    
    return GetKuisByTypeResponseModel(data=kuis_models)