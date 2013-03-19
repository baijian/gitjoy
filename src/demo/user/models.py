# -*- coding: utf-8 -*-

from sqlalchemy import Column, types
try:
    from sqlalchemy.ext.mutable import Mutable
except ImportError:
    from sqlalchemy.types import MutableTpye as Mutable
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from demo import db
from ..utils import get_current_time

class User(db.model, UserMixin):
    __tablename__ = 'users'
