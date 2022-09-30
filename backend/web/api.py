from fastapi import APIRouter
from backend.web.endpoints import users

api_router = APIRouter()
api_router.include_router(users.router, prefix='/users')
