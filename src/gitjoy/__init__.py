# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request
from .extensions import db, mail, login_manager

from .user import User, user
from .group import group
from .repo import repo
from .fork import fork
from .help import help
from .blog import blog
from .issue import issue
from .star import star
from .search import search

DEFAULT_BLUEPRINTS = (
    user,
    group,
    repo,
    fork,
    help,
    blog,
    issue,
    star,
    search,
)

def load_configuration(app):
    config = app.config

    from . import default_settings

    config.from_object(default_settings)

def configure_hook(app):
    @app.before_request
    def before_request():
        method = request.form.get('_method', '').upper()
        if method:
            request.environ['REQUEST_METHOD'] = method
            ctx = flask._request_ctx_stack.top
            ctx.url_adapter.default_method = method
            assert request.method == method

def configure_blueprints(app, blueprints=None):
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def configure_extensions(app):
    #configure the app to support the sqlalchemy db
    db.init_app(app)
    mail.init_app(app)

    login_manager.login_view = 'user.login'
    login_manager.refresh_view = 'user.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
        
    login_manager.init_app(app)

def configure_logging(app):
    if app.debug:
        import logging
        
        logger = logging.getLogger('sqlalchemy.engine')
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())

def configure_template_filters(app):
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

#Create a Flask app.
app = Flask(__name__)

load_configuration(app)
configure_hook(app)
configure_blueprints(app)
configure_extensions(app)
configure_logging(app)
configure_template_filters(app)
configure_error_handlers(app)

__all__ = []

