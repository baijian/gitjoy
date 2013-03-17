# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

#
# Configs
#
app.config.from_object("website_config")
try:
    app.config.from_pyfile(app.config['PRODUCTION_CONFIG'], silent=False)
    print '[SUCCESS] load config file: ' + app.config['PRODUCTION_CONFIG']
except:
    pass

#
# DB
#
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

#
# Login
#
@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'GET':
        if request.args.get('username'):
            error = 'same'
        else:
            error = 'different'
    return render_template('login.html', error=error)

#
# Blueprints
#
from demo.controllers import infos
app.register_blueprint(infos.mod)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


