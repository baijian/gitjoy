# -*- coding: utf-8 -*-
from sqlalchemy import or_

from ..extensions import db 
from .models import User

def create_user(username):
    user = User(username)
    db.session.add(user)
    return user

def get_user(user_id=None, **kwargs):
    if user_id is not None:
        return User.query.get(user_id)
    username = kwargs.pop("username")
    if username is not None:
        return User.query.filter_by(username=username).first()

    raise NotImplementedError

def get_user_like(query):
    return User.query.filter(or_(User.username,like('%'+query+'%'))).limit(10).all()
