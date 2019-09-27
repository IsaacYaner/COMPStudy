from flask import Flask
from server import app

@app.route("/")
def index():
    return "<h1> Hello, World </h1>"

