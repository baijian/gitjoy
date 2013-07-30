# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request

star = Blueprint('star', __name__)

@star.route('/<name>/<reponame>/star', methods = ['POST'])
def index():
    return render_template('')

