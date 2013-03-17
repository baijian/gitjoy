# -*- coding:utf-8 -*-
from demo import app, db

class Infos(db.Model):
    __tablename__ = 'infos'
    id = Column(Integer, primary_key = True)
    title = Column(String)
    text = Column(String)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    @property
    def title(self):
        return self.title

    @property
    def text(self):
        return self.text
