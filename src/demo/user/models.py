# -*- coding: utf-8 -*-

#import base64
#import struct
#import hashlib

#from sqlalchemy.orm import deferred
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, BINARY, Text, Boolean
from flask.ext.login import UserMixin

from ..extensions import db
from ..utils import get_current_time

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    display_name = Column(String(32), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    status = Column(Integer, nullable=False)
    flags = Column(Integer, nullable=False)
    creation = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)

    def __init__(self, username, display_name='', email='', status=0, flags=0):
        self.username = username
        self.display_name = display_name
        self.email = email
        self.status = status
        self.flags = flags
        self.creation = get_current_time()
        self.updated = self.creation

    def __repr__(self):
        return "<User %r(%r) - %r>" % (self.username, self.display_name, self.email)

    @property
    def name(self):
        return self.display_name or self.username
