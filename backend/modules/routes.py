from flask import request

""" flask imports """
from flask import render_template

""" Blueprint imports """
from backend.modules import views

""" Home page """
@views.route('/')
def home():
    return render_template("pages/index.html")