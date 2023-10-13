import time
import jwt
from typing import Tuple
from app.config import config

def generate_access_token(payload: str, ) -> Tuple[str, int]:
    current_time = int(time.time())
    expired_at = current_time + config.ACCESS_TOKEN_EXPIRATION
    
    payload.update({
        'exp': expired_at,
        'iat': current_time,
    })
    
    access_token = jwt.encode(payload, config.PRIVATE_KEY.encode('utf-8'), algorithm=config.ALGORITHM)
    return access_token, expired_at