# -*- coding: utf-8 -*-
import urllib, hashlib

from flask import Blueprint, render_template, request, redirect, url_for
from pygit2 import Repository
from pygit2 import init_repository

repo = Blueprint('repo', __name__)

@repo.route('/repositories/new', methods = ['GET'])
def new():
    email = "jian.baij@gmail.com"
    default = "http://en.gravatar.com/favicon.ico"
    size = 80
    img_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    img_url += urllib.urlencode({'d':default, 's': str(size)})
    return render_template("repo/new.html", img_url=img_url, username = 'baijian')

@repo.route('/repositories', methods = ['GET','POST'])
def repositories():
    if request.method == 'POST':
        username = 'baijian'
        reponame = request.form['reponame']
        repodesc = request.form['repodesc']
        init_repository('/home/git/repositories/' + username + '/' + reponame, True)
        return redirect(url_for('.index', name=username, reponame=reponame))

@repo.route('/<name>/<reponame>', methods = ['GET'])
def index(name, reponame):
    repo = Repository('/home/git/repositories/' + name + '/' + reponame)
    return render_template("repo/index.html", empty=repo.is_empty)

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

