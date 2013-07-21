# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, Markup
from flask import Blueprint, render_template

blog = Blueprint('blog', __name__)

@blog.route('/<name>/blog/')
def index(name):
    return render_template("blog/index.html")

