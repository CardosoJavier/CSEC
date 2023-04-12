""" flask imports """
from flask import Blueprint

""" declare all blueprints below """
views:Blueprint = Blueprint("views", __name__)

""" Import all view python files below """
from backend.modules import routes