from flask import render_template, request, flash, redirect, url_for
from app.module1.forms import UserForm
from app.module1 import bp
from app.module1.models import User
from flask_login import login_user, logout_user, login_required, current_user

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/1")
def index1():
    return "Basic setup, inside module 1-1"

@bp.route('/info')
def info_index():
    #return render_template('index.html')
    return "Check if route is working for module 1"