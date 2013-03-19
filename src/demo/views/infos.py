# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from demo.models.infos import Infos

mod = Blueprint("infos", __name__)

@mod.route('/info')
def h_info():
    query = Infos.query   
    results = 
    return render_template("infos/info.html", **results)
