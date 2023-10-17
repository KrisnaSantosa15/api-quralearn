import sqlalchemy as sa

from app.models import Base

class Kuis(Base):
    __tablename__ = "Kuis"
    
    # Field 	Type 	Null 	Key 	Default 	Extra 	
    # id 	int 	NO 	PRI 	NULL 	auto_increment
    # id_user 	int 	NO 	MUL 	NULL 	
    # judul 	varchar(80) 	NO 		NULL 	
    # kecepatan 	int 	NO 		NULL 	
    # ketepatan 	int 	NO 		NULL 	
    # tanggal 	date 	NO 		NULL 	
    # tipe 	enum('TEBAK_SURAH','SAMBUNG_AYAT') 	NO 		NULL 	
    
    id = sa.Column('id',sa.Integer, primary_key=True, autoincrement=True)
    id_user = sa.Column('id_user', sa.Integer, nullable=False)
    judul = sa.Column('judul', sa.String(80), nullable=False)
    kecepatan = sa.Column('kecepatan', sa.String(80), nullable=False)
    ketepatan = sa.Column('ketepatan', sa.String(80), nullable=False)
    tanggal = sa.Column('tanggal', sa.DateTime, default=sa.func.NOW())
    tipe = sa.Column('tipe', sa.Enum('TEBAK_SURAH','SAMBUNG_AYAT'), nullable=False)