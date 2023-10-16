import jwt
from typing import Optional
from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.exceptions import HTTPException

from app.utils.get_payload import get_payload

class Authentication(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        
        if not credentials:
            return {}
        
        try:
            payload = get_payload(credentials.credentials)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail={
                'message': 'Token expired',
                'code': 40100
            })
        except jwt.DecodeError:
            raise HTTPException(status_code=401, detail={
                'message': 'Token invalid',
                'code': 40101
            })
            
        return payload