import sqlalchemy as sa

from app.models import Base

class Hafalan(Base):
    __tablename__ = "Hafalan"
    
    # Field 	Type 	Null 	Key 	Default 	Extra 	
    # id 	int 	NO 	PRI 	NULL 	auto_increment
    # id_user 	int 	NO 	MUL 	NULL 	
    # judul 	varchar(70) 	NO 		NULL 	
    # tanggal 	date 	NO 		NULL 	
    # durasi 	varchar(50) 	NO 		NULL 	
    # judul_kanan 	varchar(50) 	NO 		NULL 		
    
    id = sa.Column('id',sa.Integer, primary_key=True, autoincrement=True)
    id_user = sa.Column('id_user', sa.Integer, nullable=False)
    judul = sa.Column('judul', sa.String(70), nullable=False)
    tanggal = sa.Column('tanggal', sa.DateTime, default=sa.func.NOW())
    durasi = sa.Column('durasi', sa.String(50), nullable=False)
    judul_kanan = sa.Column('judul_kanan', sa.String(50), nullable=False)