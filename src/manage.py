#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager

from demo import app
from demo.extensions import db
from demo.user import User

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
    u = User(
        username = u'baijian',
        display_name = u'baijian',
        email = u'jian.baij@gmail.com'
    )
    db.session.add(u)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
