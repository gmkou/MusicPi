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

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if '_inst' not in vars(cls):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._inst

class Player(Singleton): 
    _player = None
    def __init__(self):
        pass

    def play(self, channel):
        self.stop()
        Player._player = subprocess.Popen(["mplayer", stream_name_to_url[channel]], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    def stop(self):
        if Player._player is not None:
            Player._player.kill()

@route('/')
def index():
    return template('list_template', channels=channels)

@route('/<channel>')
def playchannel(channel):
    p = Player()
    p.play(channel)
    return template('list_template', channels=channels)

@route('/stop')
def stop():
    p = Player()
    p.stop()
    return template('list_template', channels=channels)

run(host='localhost', port=8080, debug=True, reloader=True)
