import os
from bottle import *

@route('/')
def index():
    return "Bottle forrit í pyCharm"

run(host='0.0.0.0', port=os.environ.get('PORT'))