from sqlalchemy import Column, String, Integer, Date

from base import Base


class Plant(Base):
    __tablename__ = 'plants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)