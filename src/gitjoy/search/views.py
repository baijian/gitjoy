# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request

from ..user.biz import get_user_like
from ..repo.biz import get_repo_like

search = Blueprint('search', __name__)

@search.route('/search', methods = ['GET'])
def index():
    query = request.args.get('query')
    users = get_user_like(query)
    repos = get_repo_like(query)
    return render_template('search/index.html', users=users, repos=repos)
