import uuid

from core.db import Base
from sqlalchemy import Column, String, Integer, BigInteger, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class LightingType(Base):
    __tablename__ = 'lighting_type'
    id = Column(BigInteger, primary_key=True, index=True, unique=True)
    UUID = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(100))
    watt = Column(Integer)
    connection_type = Column(String(200))


class Lighting(Base):
    __tablename__ = 'lighting'
    id = Column(BigInteger, primary_key=True, index=True, unique=True)
    UUID = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(100))
    status = Column(Boolean, default=False)
    lighting_type = Column(BigInteger, ForeignKey('lighting_type.id'))
    lighting_type_id = relationship('LightingType')
