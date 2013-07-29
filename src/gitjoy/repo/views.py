# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request
from pygit2 import Repository
from pygit2 import init_repository

repo = Blueprint('repo', __name__)

@repo.route('/<name>/<reponame>/')
def index(name, reponame):
    return render_template("repo/index.html")

@repo.route('/repositories/new', methods = ['GET'])
def new():
    return render_template("")

@repo.route('/repositories', methods = ['GET','POST'])
def repositories():
    if request.method == 'GET':
        init_repository('/home/git/repositories/baijian/test', True)
        return render_template("repo/new.html");

