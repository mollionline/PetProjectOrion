from sqlalchemy.orm import Session
from .models import LightingType
from .schemas import LightingTypeCreate


def get_light_list(db: Session):
    return db.query(LightingType).all()


def create_light(db: Session, item: LightingTypeCreate):
    light_type = LightingType(**item.dict())
    db.add(light_type)
    db.commit()
    db.refresh(light_type)
    return light_type
