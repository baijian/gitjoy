# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template, request

DEFAULT_BLUEPRINTS = (
    user,
)

def load_configuration(app):
    config = app.config

    from . import default_settings

    config.from_object(default_settings)
    if (os.environ.has_key("")):
        config.from_envvar("", silent=True)
    else:
        path = os.path.abspath(os.path.expanduser(""))
        if (os.path.isfile(path)):
            config.from_pyfile(path, silent=True)
        else:
            config.from_pyfile("/etc/demo.conf", silent=True)

def configure_logging(app):
    if app.debug:
        import logging
        
        logger = logging.getLogger('sqlalchemy.engine')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())

def configure_blueprints(app, blueprints=None):
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    for blueprint in blueprints:
        app.register_blueprints(blueprint)

def configure_templates_filters(app):
    print "test"

def configure_hook(app):
    @app.before_request
     def before_request():
         pass

def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("error.html"), 500

app = Flask(__name__)

load_configuration(app)
configure_loggings(app)
configure_blueprints(app)

##database
#from flask.ext.sqlalchemy import SQLAlchemy
#db = SQLAlchemy(app)

__all__ = []

##
## Configs
##
#app.config.from_object("website_config")
#try:
#    app.config.from_pyfile(app.config['PRODUCTION_CONFIG'], silent=False)
#    print '[SUCCESS] load config file: ' + app.config['PRODUCTION_CONFIG']
#except:
#    pass
#
##
## DB
##
#from flask.ext.sqlalchemy import SQLAlchemy
#db = SQLAlchemy(app)
#
##
## Login
##
#@app.route('/login', methods=['POST','GET'])
#def login():
#    error = None
#    if request.method == 'GET':
#        if request.args.get('username'):
#            error = 'same'
#        else:
#            error = 'different'
#    return render_template('login.html', error=error)
#
##
## Blueprints
##
#from demo.controllers import infos
#app.register_blueprint(infos.mod)
#
#
#@app.route('/hello')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)
#
#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'),404
#

