import uuid
from .models import lighting_types, lightings, LightingType
from .schemas import LightingTypeCreate, LightingTypeBase, LightingTypeList
from .schemas import LightingCreate, LightingBase, LightingList
from core.db import database


async def get_light_list():
    light_types = await database.fetch_all(query=lighting_types.select())

    lighting_type_list = LightingTypeList()
    for light_type in light_types:
        light_type = LightingTypeBase(name=light_type.name, watt=light_type.watt, UUID=light_type.UUID,
                                      connection_type=light_type.connection_type)
        lighting_type_list.items.append(light_type)
    return lighting_type_list


async def create_light(item: LightingTypeCreate):
    item.UUID = uuid.uuid4()

    light_type = lighting_types.insert().values(**item.dict())
    return await database.execute(light_type)


async def update_light(pk: int, item: LightingTypeCreate):
    light_type = lighting_types.update().where(lighting_types.c.id == pk).values(**item.dict())
    return await database.execute(light_type)


async def delete_light(pk: int):
    light_type = lighting_types.delete().where((lighting_types.c.id == pk))
    return await database.execute(light_type)


async def get_lighting_list():
    lighting_objects = await database.fetch_all(query=lightings.select())

    lighting_list = LightingList()
    for lighting_object in lighting_objects:
        lighting_object = LightingBase(UUID=lighting_object.UUID, name=lighting_object.name,
                                       status=lighting_object.status, lighting_type=lighting_object.lighting_type)
        lighting_list.items.append(lighting_object)
    return lighting_list


async def create_lighting(item: LightingCreate):
    item.UUID = uuid.uuid4()
    lighting = lightings.insert().values(**item.dict())
    return await database.execute(lighting)


async def update_lighting(pk: int, item: LightingCreate):
    lighting = lightings.update().where(lightings.c.id == pk).values(**item.dict())
    return await database.execute(lighting)


async def delete_lighting(pk: int):
    lighting = lightings.delete().where((lightings.c.id == pk))
    return await database.execute(lighting)
