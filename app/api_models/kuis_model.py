from pydantic import BaseModel
import datetime

class KuisModel(BaseModel):
    id: int
    id_user: int
    judul: str
    kecepatan: str
    ketepatan: str
    tanggal: datetime.date
    tipe: str
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "id_user": 1000,
                "judul": "Al-Fatihah",
                "kecepatan": "Sangat Baik",
                "ketepatan": "Baik",
                "tanggal": "2023-10-11",
                "tipe": "TEBAK_SURAH"
            }
        }