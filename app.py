# -*- coding: UTF-8 -*-
from flask import Flask

app = Flask(__name__)

# @app.route('/')
# @app.route('/index')
# @app.route('/home')
# def hello():
#     return 'Welcome to My Watchlist!'
# def hello():
#     return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'User page'