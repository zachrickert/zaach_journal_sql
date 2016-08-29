from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Date
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    value = Column(Integer, primary_key=True)
    name = Column(Text)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    value = Column(Integer)
    creation_date = Column(Date)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
