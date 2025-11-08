from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float


class Base(DeclarativeBase):
    pass


class City(Base):
    __tablename__ = "City"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    additional_info = Column(String, nullable=True)


class Temperature(Base):
    __tablename__ = "Temperature"
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, index=True)
    date_time = Column(String, index=True)
    temperature = Column(Float)
