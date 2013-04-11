# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app, redirect, url_for, send_from_directory
from flask.ext.login import login_required, current_user

from .forms import PubkeyForm
#from .biz import 

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<name>/')
def index(name):
    user = biz.get_user(username = name)
    if not user:
        abort(404)
    return render_template("user/index.html")

@user.route('/settings/')
def settings():
    pass

@user.route('/settings/profile')
@login_required
def profile():
    return render_template('user/profile.html')

@user.route('/settings/ssh')
@login_required
def ssh():
    pubkeys = biz.get_ssh_pubkeys(current_user.id)
    form = PubkeyForm()
    return render_template('user/ssh.html', pubkeys=pubkeys, form=form)


