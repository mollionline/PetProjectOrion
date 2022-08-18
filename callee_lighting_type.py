from autobahn.asyncio.component import Component, run
import os

from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel
from typing import List, Any, Optional

from core.db import engine
from models import *
from models.models import LightingType, Lighting, lightings, lighting_types
from core.db import database
from models.schemas import LightingCreate, LightingBase, LightingList, LightingTypeList, LightingTypeBase, \
    LightingTypeCreate
from sqlalchemy.future import select
from uuid import UUID


url = "ws://0.0.0.0:8989/public"
realmv = "ami"
print(url, realmv)
component = Component(transports=url, realm=realmv)


async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession)


@component.on_join
async def joined(session, details):
    print("session ready")

    async def get_lighting_type_list():
        async with async_session() as session:
            query = select(LightingType)

            result = (await session.scalars(query)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]

                class Config:
                    extra = 'allow'
                    orm_mode = True

            result_list = ResultList()
            for orm_lighting_type in result:
                result_list.items.append(
                    Result.from_orm(orm_lighting_type)
                )

            await session.close()

            return result_list.json()

    async def get_lighting_type_by_id(id_info):
        async with async_session() as session:
            query = select(LightingType).where(LightingType.id == int(id_info))

            result = (await session.scalars(query)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]

                class Config:
                    extra = 'allow'
                    orm_mode = True

            result_list = ResultList()
            for orm_customer in result:
                result_list.items.append(
                    Result.from_orm(orm_customer)
                )

            await session.close()

            return result_list.json()

    async def create_lighting_type(UUID, name, watt):
        async with async_session() as session:
            async with session.begin():
                session.add(
                    LightingType(UUID=UUID, name=name, watt=watt),
                )

            query = select(LightingType).where(LightingType.UUID == UUID)

            result = (await session.scalars(query)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]
                watt: Optional[int]

                class Config:
                    extra = 'allow'
                    orm_mode = True

            result_list = ResultList()
            for orm_customer in result:
                result_list.items.append(
                    Result.from_orm(orm_customer)
                )

            await session.close()

            return result_list.json()

    async def update_lighting_type(id_for_select_record, new_uuid, new_name):
        async with async_session() as session:
            query = update(LightingType).where(LightingType.id == int(id_for_select_record)).values(
                UUID=new_uuid, name=new_name)
            update_data = await session.execute(query)
            await session.commit()

            query_for_return = select(LightingType).where(LightingType.id == int(id_for_select_record))

            result = (await session.scalars(query_for_return)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]

                class Config:
                        extra = 'allow'
                        orm_mode = True

            result_list = ResultList()
            for orm_customer in result:
                result_list.items.append(
                    Result.from_orm(orm_customer)
                )

            await session.close()

            return result_list.json()

    async def delete_lighting_type(id_for_delete):
        async with async_session() as session:
            query = delete(LightingType).where(LightingType.id == int(id_for_delete))
            delete_data = await session.execute(query)
            await session.commit()

            await session.close()

            return 'LightingType WITH ID:{} HAS BEEN DELETED'.format(id_for_delete)



    try:
        await session.register(get_lighting_type_list, 'get_lighting_type_list')
        await session.register(get_lighting_type_by_id, 'get_lighting_type_by_id')
        await session.register(create_lighting_type, 'create_lighting_type')
        await session.register(update_lighting_type, 'update_lighting_type')
        await session.register(delete_lighting_type, 'delete_lighting_type')

        print("get_lighting_type_list - registered")
        print("get_lighting_type_by_id - registered")
        print("create_lighting_type - registered")
        print("update_lighting_type - registered")
        print("delete_lighting_type - registered")

    except Exception as e:
        print("could not register procedure: {0}".format(e))


if __name__ == "__main__":
    run([component])        



