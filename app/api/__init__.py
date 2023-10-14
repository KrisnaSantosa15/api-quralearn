from fastapi import APIRouter
from app.api.auth.auth_register import auth_register
from app.api.auth.auth_login import auth_login, LoginResponseModel

api_router = APIRouter()

api_router.add_api_route("/api/v1/auth/register", auth_register, methods=["POST"], tags=["auth"], status_code=201)
api_router.add_api_route("/api/v1/auth/login", auth_login, methods=["POST"], tags=["auth"], response_model=LoginResponseModel)