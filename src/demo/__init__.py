# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object("website_config")

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'GET':
        if request.args.get('username'):
            error = 'same'
        else:
            error = 'different'
    return render_template('login.html', error=error)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


