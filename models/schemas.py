from pydantic import BaseModel


class LightingTypeBase(BaseModel):
    name: str
    watt: int
    # UUID: int

    class Config:
        orm_mode = True


class LightingTypeList(LightingTypeBase):
    id: int


class LightingTypeCreate(LightingTypeBase):
    pass



