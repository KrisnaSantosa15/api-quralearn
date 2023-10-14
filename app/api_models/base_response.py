from typing import Any
from pydantic import BaseModel

class BaseResponseModel(BaseModel):
    data: Any = {}
    meta: dict = {}
    success: bool = True
    code: int = 200
    message: str = "Success"

