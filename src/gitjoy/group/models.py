# -*- coding: utf-8 -*-
from sqlalchemy.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer, String, Text, DateTime

from ..extensions import db 
from ..utils import get_current_time

class Group():
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    group_name = Column(String(255), nullable=False)
    group_desc = Column(String(900))
    creation = Column(DateTime, nullable=False)
    
    def __init__(self, owner_id, group_name):
        self.owner_id = owner_id
        self.group_name = group_name
        self.creation = get_current_time

