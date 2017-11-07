import os
from bottle import *

@route('/')
def index():
    return "Bottle forrit í pyCharm bla bla "

run(host='0.0.0.0', port=os.environ.get('PORT'))