from flask import request

""" flask imports """
from flask import render_template

""" Blueprint imports """
from backend.modules import views

""" Home page """
@views.route('/')
def home():
    return render_template("pages/index.html")

""" About page """
@views.route('/about')
def about():
    return render_template("pages/about.html", 
                           head1="Welcome to UT Arlington's", 
                           head2="Cybersecurity Club",
                           bg="about/about.svg")

""" Calendar page """
@views.route('/caledar')
def calendar():
    return render_template("pages/calendar.html", 
                           head1="Stay up to date with all of our events", 
                           head2="by checking out our calendar", 
                           bg="calendar/calendar.svg")

""" Gallery page """
@views.route('/gallery')
def gallery():
    return render_template("pages/gallery.html", 
                           head1="CSEC", 
                           head2="Throughtout the Years", 
                           bg="gallery/gallery.svg")