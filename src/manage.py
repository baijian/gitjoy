#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager

from gitjoy import app
from gitjoy.extensions import db
from gitjoy.user import User
from gitjoy.repo import Repo

manager = Manager(app)

@manager.command
def hello():
    print "Hello man, Welcome~."

@manager.command
def initdb():
    '''Init/reset database.'''
    db.drop_all()
    db.create_all()
    u = User(
        username = u'baijian',
        display_name = u'baijian',
        email = u'jian.baij@gmail.com'
    )
    db.session.add(u)
    db.session.commit()

@manager.command
def run():
    '''Run local server.'''
    app.run()

if __name__ == '__main__':
    manager.run()

