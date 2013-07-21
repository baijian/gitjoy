# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, Markup
from flask import Blueprint, render_template

group = Blueprint('group', __name__)

@group.route('/groups')
def index():
    return render_template("group/index.html")
