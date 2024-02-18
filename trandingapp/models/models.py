from datetime import datetime
from sqlalchemy import JSON, MetaData, Integer, String, TIMESTAMP, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

metadata = MetaData()

class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=False)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey('roles.id'))