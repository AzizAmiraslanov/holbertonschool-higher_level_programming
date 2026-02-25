#!/usr/bin/python3
"""State class definition using SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create declarative base
Base = declarative_base()

class State(Base):
    """State class mapping to 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)