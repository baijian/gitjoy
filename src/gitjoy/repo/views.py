# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request
from pygit2 import Repository
from pygit2 import init_repository

repo = Blueprint('repo', __name__)

@repo.route('/repositories/new', methods = ['GET'])
def new():
    return render_template("")

@repo.route('/repositories', methods = ['GET','POST'])
def repositories():
    if request.method == 'GET':
        init_repository('/home/git/repositories/baijian/test', True)
        return render_template("repo/new.html");

@repo.route('/<name>/<reponame>', methods = ['GET'])
def index(name, reponame):
    repo = Repository('/home/git/repositories/' + name + '/' + reponame + '/.git')
    if repo.is_empty:
        return render_template('repo/index.html')
    return render_template("repo/index.html")

@repo.route('/<name>/<reponame>/commits/<branch>', methods = ['GET'])
def commits():
    return render_template("")

@repo.route('/<name>/<reponame>/commit/<sha>', methods = ['GET'])
def commit():
    return render_template('')

@repo.route('/<name>/<reponame>/tree/<branch>/<treename>', methods = ['GET'])
def tree():
    return render_template('')

@repo.route('/<name>/<reponame>/blob/<branch>/<blobname>', methods = ['GET'])
def blob():
    return render_template('')

