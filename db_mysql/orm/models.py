"""
Create engine
Create session
Create table
Migrate
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()


class Student(Base):
    """
    Student Model
    This for mapping to DB table
    """
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer)
    grade = Column(String(50))


# migration of Model to table in DB
Base.metadata.create_all(engine)
