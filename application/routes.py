from flask import render_template, url_for
from flask import Flask
from flask import current_app as app

@app.route('/')
def home():
    return render_template("index.html")
