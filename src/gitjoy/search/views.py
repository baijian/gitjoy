# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

search = Blueprint('search', __name__)

@search.route('/search', methods = ['GET'])
def index():
    return render_template('')
