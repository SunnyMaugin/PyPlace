from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        message="Welcome to PyPlace, please have a look around and try the features available toy ou to get started with Python"
        )



