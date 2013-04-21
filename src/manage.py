#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.script import Manager

from gitonion import app
#from gitonion.extensions import db
#from gitonion.user import User

manager = Manager(app)

@manager.command
def hello():
    print "Hello, Welcome to help develop gitonion."

#@manager.command
#def initdb():
#    '''Init/reset database.'''
#    db.drop_all()
#    db.create_all()
#    u = User(
#        username = u'baijian',
#        display_name = u'baijian',
#        email = u'jian.baij@gmail.com'
#    )
#    db.session.add(u)
#    db.session.commit()

@manager.command
def run():
    '''Run local server.'''
    app.run()

if __name__ == '__main__':
    manager.run()
