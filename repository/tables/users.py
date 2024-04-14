from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    def __init__(self, id, name, surname, username, password, email):
        self.id = id
        self.username = username
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email