import sqlalchemy as sa
from fastapi import Depends, Response, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from app.dependencies.get_db_session import get_db_session
from app.models.waiting_list import WaitingList

class WaitingListData(BaseModel):
    email: str

async def waiting_list(data: WaitingListData, session = Depends(get_db_session)):
    
    # check if email is already exist
    check_email = session.execute(sa.select(WaitingList.id).where(WaitingList.email == data.email)).scalar_one_or_none()
    if check_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='username already taken')
    
    waiting_list = WaitingList(
            email=data.email
        )
    session.add(waiting_list)
    session.commit()
    
    return Response(status_code=status.HTTP_201_CREATED)