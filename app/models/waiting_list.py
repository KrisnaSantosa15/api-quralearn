import sqlalchemy as sa

from app.models import Base

class WaitingList(Base):
    __tablename__ = "WaitingList"
    
    # Field 	Type 	Null 	Key 	Default 	Extra 	
    # id 	int 	NO 	PRI 	NULL 	auto_increment
    # email 	varchar(255) 	NO 		NULL
    id = sa.Column('id',sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column('email', sa.String(255), nullable=False, unique=True)