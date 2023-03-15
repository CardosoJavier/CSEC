from flask import request

""" flask imports """
from flask import render_template

""" Blueprint imports """
from backend.modules import views

""" Home page """
@views.route('/')
def home():
    return render_template("home_page.html")

""" About page """
@views.route('/about')
def about():
    return render_template("about_page.html")

""" Calendar page """
@views.route('/calendar')
def calendar():
    return render_template("calendar_page.html")

""" Gallery page """
@views.route('/gallery')
def gallery():
    return render_template("gallery_page.html")