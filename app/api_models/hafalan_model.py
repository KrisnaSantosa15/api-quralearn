from pydantic import BaseModel
import datetime

class HafalanModel(BaseModel):
    id: int
    judul: str
    tanggal: datetime.date
    durasi: str
    judul_kanan: str
    id_user: int
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "judul": "Al-Fatihah",
                "tanggal": "2023-10-11",
                "durasi": "00:00:00",
                "judul_kanan": "Al-Fatihah",
                "id_user": 1000
            }
        }