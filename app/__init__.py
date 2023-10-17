from fastapi import FastAPI
from app.api import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with a list of allowed origins
    allow_methods=["*"],  # Replace "*" with a list of allowed methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Replace "*" with a list of allowed headers
    allow_credentials=True,
)


app.include_router(api_router)