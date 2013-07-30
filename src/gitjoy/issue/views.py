# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request

issue = Blueprint('issue', __name__)

@issue.route('/<name>/<reponame>/issues', methods = ['GET', 'POST', 'PATCH'])
def issues():
    return render_template('')

@issue.route('/<name>/<reponame>/new', methods = ['GET'])
def new():
    return render_template('')
