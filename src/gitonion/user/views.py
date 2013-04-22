# -*- coding: utf-8 -*-

import urllib, hashlib

from flask import Blueprint, render_template, current_app, redirect, url_for, send_from_directory
from flask.ext.login import login_required, current_user

from .forms import PubkeyForm, LoginForm
#from .biz import 

user = Blueprint('user', __name__)

@user.route('/login', methods = ['POST'])
def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash("logged in successfully.")
#        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html")

@user.route('/<name>/')
def index(name):
#    user = biz.get_user(username = name)
#    if not user:
#        abort(404)
    email = "bj@xiaocong.tv"
    default = "http://en.gravatar.com/favicon.ico"
    size = 80
    img_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    img_url += urllib.urlencode({'d':default, 's': str(size)})
    return render_template("user/index.html", img_url=img_url, username = 'baijian')

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


