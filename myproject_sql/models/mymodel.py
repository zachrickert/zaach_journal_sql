from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    value = Column(Integer, primary_key=True)
    name = Column(Text)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(UnicodeText)
    value = Column(Integer)
    creation_date = Column(DateTime)


# Index('my_index', Entry.title, unique=True, mysql_length=255)
