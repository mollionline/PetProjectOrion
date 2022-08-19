from autobahn.asyncio.component import Component, run

from sqlalchemy import update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from pydantic import BaseModel
from typing import List, Any, Optional

from core.db import engine
from models.models import Lighting
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

    async def get_lighting_list():
        async with async_session() as session:
            query = select(Lighting)

            result = (await session.scalars(query)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]
                status: Optional[bool]

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

    async def get_lighting_by_id(id_info):
        async with async_session() as session:
            query = select(Lighting).where(Lighting.id == int(id_info))

            result = (await session.scalars(query)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]
                status: Optional[bool]

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

    async def create_lighting(UUID, name, status):
        async with async_session() as session:
            async with session.begin():
                session.add(
                    Lighting(UUID=UUID, name=name, status=status),
                )

            query = select(Lighting).where(Lighting.UUID == UUID)

            result = (await session.scalars(query)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: Optional[str]
                status: Optional[bool]

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

    async def update_lighting(id_for_select_record, new_uuid, name, status):
        async with async_session() as session:
            query = update(Lighting).where(Lighting.id == int(id_for_select_record)).values(UUID=new_uuid, name=name, status=status)
            update_data = await session.execute(query)
            await session.commit()

            query_for_return = select(Lighting).where(Lighting.id == int(id_for_select_record))

            result = (await session.scalars(query_for_return)).all()

            class ResultList(BaseModel):
                items: List[Any] = []

            class Result(BaseModel):
                UUID: Optional[UUID]
                name: str
                status: Optional[bool]

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

    async def delete_lighting(id_for_delete):
        async with async_session() as session:
            query = delete(Lighting).where(Lighting.id == int(id_for_delete))
            delete_data = await session.execute(query)
            await session.commit()

            await session.close()

            return 'LightingType WITH ID:{} HAS BEEN DELETED'.format(id_for_delete)

    try:
        await session.register(get_lighting_list, 'get_lighting_list')
        await session.register(get_lighting_by_id, 'get_lighting_by_id')
        await session.register(create_lighting, 'create_lighting')
        await session.register(update_lighting, 'update_lighting')
        await session.register(delete_lighting, 'delete_lighting')

        print("get_lighting_list - registered")
        print("get_lighting_by_id - registered")
        print("create_lighting - registered")
        print("update_lighting - registered")
        print("delete_lighting_type - registered")

    except Exception as e:
        print("could not register procedure: {0}".format(e))


if __name__ == "__main__":
    run([component])
