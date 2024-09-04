from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    tax = Column(Float, default=0)


class Pipocas(Base):
    __tablename__ = "popcorns"

    id = Column(Integer, primary_key=True, index=True)
    create_on = Column(String, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    weight = Column(Float)
    quantity = Column(Float)