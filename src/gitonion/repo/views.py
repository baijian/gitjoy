# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

repo = Blueprint('repo', __name__)

@repo.route('/<name>/<reponame>/')
def index(name, reponame):
    return render_template("repo/index.html")
