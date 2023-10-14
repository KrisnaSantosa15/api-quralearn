from functools import lru_cache
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    #ACCESS_TOKEN_EXPIRATION: int = 60 * 60 * 24 * 7 # 7 days
    ACCESS_TOKEN_EXPIRATION: int = 5 * 60 # 5 minutes
    REFRESH_TOKEN_EXPIRATION: int = 60 * 60 * 24 * 30 # 30 days
    
    PRIVATE_KEY: str
    PUBLIC_KEY: str
    REFRESH_PRIVATE_KEY: str
    ALGORITHM: str = 'RS256'
    
    DB: str
    DB_POOL_PRE_PING: bool = True
    DB_POOL_SIZE: int = 20
    DB_POOL_RECYCLE: int = 1800 # 30 minutes
    DB_ECHO: bool = False
    
    class Config:
        env_file = ".env"
        
        
@lru_cache
def get_config():
    return Config()

config = get_config()