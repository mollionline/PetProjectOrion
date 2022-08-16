from fastapi import APIRouter
from models import light

routes = APIRouter()

routes.include_router(light.router, prefix='/light')
