# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, Markup
from ..utils import markdown_to_html
from .models import get_help_info

help = Blueprint('help', __name__)

@help.route('/help')
def index():
    contents = Markup(markdown_to_html(get_help_info()))
    return render_template("help/index.html", contents=contents)
