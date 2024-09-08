from flask import Blueprint, render_template

root = Blueprint(__name__, "root")


@root.route("/")
def home():
    return render_template('home.html')
