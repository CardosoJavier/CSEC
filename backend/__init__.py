from flask import Flask

def create_app():

    """ App settings """
    app:Flask = Flask(__name__)
    app.config['SECRET_KEY'] = 'mySecret!'

    """ init apps """

    """ blueprints """
    from backend.modules import views

    app.register_blueprint(views)

    """ database settings """

    """ login manager settings """

    # return the built app from above
    return app