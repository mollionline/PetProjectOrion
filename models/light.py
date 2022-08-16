from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .schemas import LightingTypeCreate

router = APIRouter()


@router.get('/')
def post_list(db: Session = Depends(get_db)):
    return service.get_light_list(db)


@router.post('/')
def post_list(item: LightingTypeCreate, db: Session = Depends(get_db)):
    return service.create_light(db, item)
