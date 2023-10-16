from pydantic import BaseModel


class ProfileModel(BaseModel):
    id: int
    username: str
    full_name: str