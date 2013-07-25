# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, Markup
from flask import Blueprint, render_template

group = Blueprint('group', __name__)

@group.route('/groups', methods = ["GET","POST"])
def index():
    if request.method == 'POST':
        return render_template("group/index.html")   
    elif request.method =='GET':
        return render_template("group/index.html")
    return render_template("group/index.html")

@group.route('/groups/<id>/')
def delete():
    return render_template("")
