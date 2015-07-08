#!/usr/bin/env python
#coding:utf-8
import bottle
bottle.debug(True)
import socket

import qrcode
import qrcode.image.svg

from bottle import route, run, template, static_file
import subprocess, re, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
hostip = s.getsockname()[0]

protocol = "http"
port = "8080"
host = hostip

fifo = "/tmp/mplayercontrol"
if os.path.exists(fifo):
    os.unlink(fifo)
os.mkfifo(fifo)

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
    _volume = 50
    def __init__(self):
        pass

    def play(self, channel):
        self.stop()
        Player._player = subprocess.Popen(["mplayer", stream_name_to_url[channel],  "-slave", "-quiet", "-input", "file=/tmp/mplayercontrol" ], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def title(self):
        p = re.compile(r".*StreamTitle.*")
        while True:
            line = Player._player.stdout.readline()
            if p.match(line): 
                return line.split(':')[1].split(';')[0].split('=')[1]

    def stop(self):
        if Player._player is None:
            return
        Player._player.poll()
        if Player._player.returncode is None:
            Player._player.communicate('quit\n')

    def volume(self, to):
        if to == 'increase':
            Player._volume += 5
        elif to == 'decrease':
            Player._volume -= 5
        else:
            Player._volume += 0
        os.system('echo "volume %d 1" > %s' % (Player._volume, fifo))


@route('/')
def index():
    return template('list_template', channels=channels)

@route('/<channel>', method='GET')
def playchannel(channel="main"):
    p = Player()
    p.play(channel)
    out = p.title()
    return { "success" : True, "StreamTitle" : out } 

@route('/stop', method='GET')
def stop():
    p = Player()
    p.stop()
    return { "success" : True } 

@route('/volume/<to>', method='GET')
def volume(to="none"):
    p = Player()
    p.volume(to)
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

run(host=host, port=port, debug=True, reloader=True)
