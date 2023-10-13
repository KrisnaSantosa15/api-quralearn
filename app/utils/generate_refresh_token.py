import time
import jwt
from app.config import config


def generate_refresh_token(payload: str) -> str:
    current_time = int(time.time())
    
    payload.update({
        'iat': current_time
    })
    
    refresh_token = jwt.encode(payload, config.REFRESH_PRIVATE_KEY.encode('utf-8'), algorithm=config.ALGORITHM)
    
    return refresh_token