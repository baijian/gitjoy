# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request

fork = Blueprint('fork', __name__)

@fork.route('/fork', methods = ['POST'])
def index():
    return render_template('')


