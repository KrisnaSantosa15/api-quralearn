import sqlalchemy as sa
from fastapi import Depends, Response, status
from pydantic import BaseModel

from app.dependencies.get_db_session import get_db_session
from app.models.waiting_list import WaitingList

class WaitingListData(BaseModel):
    email: str

async def waiting_list(data: WaitingListData, session = Depends(get_db_session)):
    
    waiting_list = WaitingList(
            email=data.email
        )
    session.add(waiting_list)
    session.commit()
    
    return Response(status_code=status.HTTP_201_CREATED)