# -*- coding: utf-8 -*-
from sqlalchemy.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.types import Integer, String, Text, DateTime
from sqlalchemy.orm import deferred
from datetime import datetime

from ..extensions import db 

def enum(*sequential, **named):
        mapping = dict(zip(sequential, range(len(sequential))), **named)

        enums = {}
        enums['values'] = sorted(mapping.values())
        enums['reverse_mapping'] = dict((value, key) for key, value in mapping.iteritems())
        enums.update(mapping)

        return type('Enum', (), enums)

class Issue(db.Model):
    __tablename__ = 'issues'

    Status = enum(OPEN='open', CLOSED='closed', DELETED='deleted')
    Label = enum(BUG='bug', DUPLICATE='duplicate', \
            ENHANCEMENT='enhancement', INVALID='invalid', \
            QUESTION='question', WONTFIX='wontfix')

    id = Column(Integer, primary_key=True)
    repo_id = Column(Integer)
    creator_id = Column(Integer)
    assign_id = Column(Integer)
    title = Column(String)
    content = deferred(Column(Text))
    labels = Column(String)
    status = Column(String)
    create_time = Column(DateTime)

    def __init__(self, repo_id, creator_id, assign_id, title,\
            content, labels):
        self.repo_id = repo_id
        self.creator_id = creator_id
        self.assign_id = assign_id
        self.title = title
        self.content = content
        self.labels = labels
        self.status = Issue.Status.OPEN
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Issue %s/%s>' % (self.id, self.title)
