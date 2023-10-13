import sqlalchemy as sa

from app.models import Base

class User(Base):
    __tablename__ = "User"
    
    #     id 	int 	NO 	PRI 	NULL 	auto_increment
    # username 	varchar(256) 	NO 	MUL 	NULL 	
    # password 	varchar(512) 	NO 		NULL 	
    # full_name 	varchar(256) 	YES 			
    # created_at 	datetime 	NO 		CURRENT_TIMESTAMP 	DEFAULT_GENERATED
    # modified_at 	datetime 	NO 		CURRENT_TIMESTAMP 	DEFAULT_GENERATED

    id = sa.Column('id',sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column('username', sa.String(256), nullable=False, unique=True)
    password = sa.Column('password', sa.String(512), nullable=False)
    full_name = sa.Column('full_name', sa.String(256), nullable=True)
    created_at = sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now())
    modified_at = sa.Column('modified_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())
    