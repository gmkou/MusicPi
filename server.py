#!/usr/bin/env python
#coding:utf-8
import bottle
bottle.debug(True)

from bottle import route, run, template, error
import os.path

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/list')
def list():
    music_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'music')
    files = []
    if os.path.exists(music_dir):
        files = os.listdir(music_dir)

    return template('list_template', files=files)

run(host='localhost', port=8080, debug=True, reloader=True)
