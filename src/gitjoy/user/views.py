# -*- coding: utf-8 -*-

import urllib, hashlib

from flask import Blueprint, render_template, current_app, redirect, url_for, send_from_directory
from flask.ext.login import login_required, current_user

from .forms import PubkeyForm, LoginForm
from .biz import get_user
from .models import User

user = Blueprint('user', __name__)

#@user.route('/newissue/', methods = ["GET", "POST"])
#def newissue():
#    form = LoginForm()
#    if form.validate_on_submit():
#
#    return render_template("user/login.html", form=form, )

@user.route('/login', methods = ["GET","POST"])
def login():
    """
    Login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Welcome %s' % user.username)
            #return redirect(request.args.get("next") or url_for("index",name=user.username))
            return redirect(url_for("index",name=user.username))
        flash('Wrong email or password', 'error-message')
    return render_template("user/login.html", form=form)

@user.route('/<name>/')
@login_required
def index(name):
    user = get_user(username = name)
    if not user:
        abort(404)
    email = "jian.baij@gmail.com"
    default = "http://en.gravatar.com/favicon.ico"
    size = 80
    img_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    img_url += urllib.urlencode({'d':default, 's': str(size)})
    return render_template("user/index.html", img_url=img_url, username = 'baijian')

@user.route('/settings/')
@login_required
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

#@user.route('/logout')
#@login_required
#     logout_user()
#     return redirect(url_for("login"))

