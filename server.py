#!/usr/bin/env python
#coding:utf-8
import bottle
bottle.debug(True)

from bottle import route, run, template, error, redirect
import subprocess, sys, re

channels = ["main", "random", "rock", "metal", "indie"]
stream_name_to_url = {
    "main": "http://173.231.136.91:8000/",
    "random": "http://173.231.136.91:8050/",
    "rock": "http://173.231.136.91:8020/",
    "metal": "http://173.231.136.91:8090/",
    "indie": "http://173.231.136.91:8070/"
}

@route('/')
def index():
    redirect("/main")

@route('/<stream_name>')
def list(stream_name):
    player = subprocess.Popen(["mplayer", stream_name_to_url[stream_name]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    return template('list_template', channels=channels)

run(host='localhost', port=8080, debug=True, reloader=True)
