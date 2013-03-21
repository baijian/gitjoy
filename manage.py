#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask.ext.script import Manager
from demo import app
from demo.extensions import db

manager = Manager(app)

@manager.command
def run():
    '''Run local server.'''
    app.run()

@manager.command
def initdb():
    '''Init/reset database.'''
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
