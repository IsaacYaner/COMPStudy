from flask import Flask, redirect, render_template, request
from server import app

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        desc = request.form["desc"]
        return render_template("hello.html", name=name, id=zID, desc=desc)
    return render_template("index.html")

@app.route("/Hello/<name>/<id>/<desc>")
def hello(name, id, desc):
    return render_template("hello.html", name=name, id=id, desc=desc)

