from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional


class LightingTypeBase(BaseModel):
    name: str
    watt: int
    UUID: Optional[UUID]
    connection_type: Optional[str]


class LightingTypeList(BaseModel):
    items: List[LightingTypeBase] = []


class LightingTypeCreate(LightingTypeBase):
    class Config:
        orm_mode = True


class LightingBase(BaseModel):
    UUID: Optional[UUID]
    name: str
    status: Optional[bool]
    lighting_type: Optional[int]


class LightingList(BaseModel):
    items: List[LightingBase] = []


class LightingCreate(LightingBase):
    class Config:
        orm_mode = True
