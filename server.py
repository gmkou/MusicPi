#!/usr/bin/env python
#coding:utf-8
import bottle
bottle.debug(True)
import socket

import qrcode
import qrcode.image.svg

from bottle import route, run, template, error, redirect, static_file
import subprocess, sys, re, os, signal

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
hostip = s.getsockname()[0]

protocol = "http"
port = "8080"
host = hostip

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
        Player._player = subprocess.Popen(["mplayer", stream_name_to_url[channel],  "-slave", "-quiet"], shell=False, stdin=subprocess.PIPE,  stderr=subprocess.PIPE)
                    
    def stop(self):
        if Player._player is None:
            return
        Player._player.poll()
        if Player._player.returncode is None:
            Player._player.communicate('quit\n')

@route('/')
def index():
    return template('list_template', channels=channels)

@route('/<channel>', method='GET')
def playchannel(channel="main"):
    p = Player()
    p.play(channel)
    return { "success" : True } 

@route('/stop', method='GET')
def stop():
    p = Player()
    p.stop()
    return { "success" : True } 

@route('/qr')
def qr():
    url = protocol + "://" + host + ":" + port
    img = qrcode.make(url)
    img.save('image/qrcode.png')
    return template('qr_template', url=url)

@route('/image/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./image')

@route('/favicon.ico')
def favicon():
    return static_file("favicon.ico", root="./")

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

run(host=host, port=port, debug=True, reloader=True)
