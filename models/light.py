from fastapi import APIRouter
from . import service
from .schemas import LightingTypeCreate, LightingCreate, LightingBase

router = APIRouter()


@router.get('/types')
async def light_type_list():
    return await service.get_light_list()


@router.post('/create')
async def light_type_create(item: LightingTypeCreate):
    return await service.create_light(item)


@router.put('/update')
async def light_type_update(pk: int, item: LightingTypeCreate):
    return await service.update_light(pk, item)


@router.delete("/{pk}", status_code=204)
async def light_type_delete(pk: int):
    return await service.delete_light(pk)


@router.get("/{lighting_type_id}")
async def get_lighting_type_by_id(lighting_type_id: int):
    return await service.get_by_id_lighting_type(lighting_type_id)


@router.get('/lightings')
async def lighting_list():
    return await service.get_lighting_list()


@router.post('/create/lighting', status_code=201)
async def lighting_create(item: LightingCreate):
    return await service.create_lighting(item)


@router.put('/update/lighting')
async def lighting_update(pk: int, item: LightingCreate):
    return await service.update_lighting(pk, item)


@router.delete("/{pk}/lighting", status_code=204)
async def lighting_delete(pk: int):
    return await service.delete_lighting(pk)


@router.get("/{lighting_id}")
async def get_lighting_by_id(lighting_id: int):
    return await service.get_by_id_lighting(lighting_id)
