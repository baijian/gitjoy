# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, Markup
from flask import Blueprint, render_template

group = Blueprint('group', __name__)

@group.route('/groups', methods = ["GET","POST"])
def groups():
    if request.method == 'POST':
        return render_template("group/index.html")   
    elif request.method =='GET':
        return render_template("group/index.html")

@group.route('/groups/<id>', methods = ["GET"])
def index():
    return render_template("group/index.html")

@group.route('/groups/new', methods = ["GET"])
def new():
    return render_template("group/index.html")

