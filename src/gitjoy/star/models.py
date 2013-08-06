# -*- coding: utf-8 -*-
from sqlalchemy.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer, String, Text, DateTime

from ..extensions import db 

class Star(db.Model):
    __tablename__ = 'stars'

    id = Column(Integer, primary_key = True)
    repo_id = Column(Integer)
    user_id = Column(Integer)
    create_time = Column(DateTime)

    def __init__(self, repo_id, user_id):
        self.repo_id = repo_id
        self.user_id = user_id
        
    def __repr__(self):
        return '<Watch %s/%d>' % (self.id, self.repo_id)
