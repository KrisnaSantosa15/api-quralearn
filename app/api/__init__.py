from fastapi import APIRouter

from app.api.auth.auth_register import auth_register
from app.api.auth.auth_login import auth_login, LoginResponseModel
from app.api.auth.auth_logout import auth_logout
from app.api.auth.auth_refresh_token import auth_refresh_token, RefreshTokenResponseModel
from app.api.auth.get_profile import get_profile, GetProfileResponseModel
from app.api.auth.edit_profile import edit_profile

from app.api.quran.quran_recognizer import quran_recognizer
from app.api.quran.quran_hafalan import quran_hafalan
from app.api.quran.get_hafalan import get_hafalan, GetHafalanResponseModel
from app.api.quran.quran_kuis import quran_kuis, KuisResponseModel

from app.api.inspiration.get_funfacts import get_funfacts, GetFunfactsResponseModel
from app.api.inspiration.get_quotes import get_quotes, GetQuotesResponseModel

api_router = APIRouter()

# AUTH ROUTES
api_router.add_api_route("/api/v1/auth/register", auth_register, methods=["POST"], tags=["auth"], status_code=201)
api_router.add_api_route("/api/v1/auth/login", auth_login, methods=["POST"], tags=["auth"], response_model=LoginResponseModel)
api_router.add_api_route("/api/v1/auth/logout", auth_logout, methods=["POST"], tags=["auth"], status_code=204)
api_router.add_api_route("/api/v1/auth/refresh-token", auth_refresh_token, methods=["POST"], tags=["auth"], response_model=RefreshTokenResponseModel)
api_router.add_api_route("/api/v1/auth/profile", get_profile, methods=["GET"], tags=["auth"], response_model=GetProfileResponseModel)
api_router.add_api_route("/api/v1/auth/profile", edit_profile, methods=["PUT"], tags=["auth"], status_code=204)

# QURAN ROUTES
api_router.add_api_route("/api/v1/quran/recognizer", quran_recognizer, methods=["POST"], tags=["quran"], status_code=201)
api_router.add_api_route("/api/v1/quran/hafalan", quran_hafalan, methods=["POST"], tags=["quran"], status_code=201)
api_router.add_api_route("/api/v1/quran/hafalan", get_hafalan, methods=["GET"], tags=["quran"], response_model=GetHafalanResponseModel)
api_router.add_api_route("/api/v1/quran/kuis", quran_kuis, methods=["POST"], tags=["quran"], response_model=KuisResponseModel)

# INSPIRATION ROUTES
api_router.add_api_route("/api/v1/inspiration/funfacts", get_funfacts, methods=["GET"], tags=["inspiration"], response_model=GetFunfactsResponseModel)
api_router.add_api_route("/api/v1/inspiration/quotes", get_quotes, methods=["GET"], tags=["inspiration"], response_model=GetQuotesResponseModel) 