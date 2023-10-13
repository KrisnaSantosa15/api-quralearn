import sqlalchemy as sa

from app.models import Base

class UserLogin(Base):
    __tablename__ = "UserLogin"
    
    #id 	int 	NO 	PRI 	NULL 	auto_increment
    #user_id 	int 	NO 	MUL 	NULL 	
    #refresh_token 	varchar(512) 	NO 	MUL 	NULL 	
    #expired_at 	datetime 	NO 		CURRENT_TIMESTAMP 	DEFAULT_GENERATED
    #created_at 	datetime 	NO 		CURRENT_TIMESTAMP 	DEFAULT_GENERATED
    #modified_at 	datetime 	NO 		CURRENT_TIMESTAMP 	DEFAULT_GENERATED
    
    id = sa.Column('id',sa.Integer, primary_key=True, autoincrement=True)
    user_id = sa.Column('user_id', sa.Integer, nullable=False)
    refresh_token = sa.Column('refresh_token', sa.String(512), nullable=False)
    expired_at = sa.Column('expired_at', sa.DateTime, nullable=False, server_default=sa.func.now())
    created_at = sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now())
    modified_at = sa.Column('modified_at', sa.DateTime, nullable=False, server_default=sa.func.now(), onupdate=sa.func.now())