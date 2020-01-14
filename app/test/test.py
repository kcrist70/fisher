
from flask import Flask, current_app, request

app = Flask(__name__)
d = request.args.to_dict()
ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']

with open('a',"r") as f:
    pass