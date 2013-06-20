# -*- coding: utf-8 -*-
from sqlalchemy.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer, String, Text, DateTime

from ..extensions import db 
from ..utils import get_current_time

class Repo(db.Model):
    __tablename__ = "repos"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)

    forked_from_id = Column(Integer, ForeignKey("repos.id"), nullable=False)
    master_branch = Column(String(255), nullable=False)

    status = Column(Integer, nullable=False)
    flags = Column(Integer, nullable=False)
    creation = Column(DateTime, nullable=False)
    updated = Column(DateTime, nullable=False)

    __table_args__ = (UniqueConstraint("user_id","name", name="user_repos"),)

    def init(self, name, user_id, description="", status=0, flags=0):
        self.name = name
        self.user_id = user_id
        self.description = description

        self.forked_from_id = 0
        self.master_branch = 0

        self.status = status
        self.flags = flags
        self.creation = get_current_time()
        self.updated = self.creation

    def __repr__(self):
        return "<Repo %r: %r/%r>" % (self.id, self.user.username, self.name)

