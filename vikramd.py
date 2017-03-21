
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file, response, request, template
from urllib import quote
from datetime import datetime
import json
import os

# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@route('/')
def index():
    return static_file('index.html', root='/home/vik1124/vikramd/templates')

@route('/js/<filename>')
def getJSfile(filename):
    return static_file(filename, root='/home/vik1124/vikramd/templates')

@route('/static/<filename>')
def getStaticfile(filename):
    return static_file(filename, root='/home/vik1124/vikramd/css')

application = default_app()

