#!/usr/bin/python3
"""
Module to hold a class to define city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    Class to defin what a city is
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
