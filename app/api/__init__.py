from fastapi import APIRouter
from app.api.auth.auth_register import auth_register
api_router = APIRouter()

api_router.add_api_route("/api/v1/auth/register", auth_register, methods=["POST"], tags=["auth"], status_code=201)