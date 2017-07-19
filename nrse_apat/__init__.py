import os
from flask import Flask, redirect, url_for
from flask_security import login_required

# Initialising variables
app = None

import nrse_apat.database
from nrse_apat import auth
from nrse_apat.config import config

from nrse_apat.homepage.views import homepage_blueprint
from nrse_apat.actions.views import actions_blueprint
from nrse_apat.initiatives.views import initiatives_blueprint

def create_app(name, environment=None):

    # Select config mode
    if environment is None:
        environment = 'development'

    # Create Flask app
    app = Flask(name, template_folder='nrse_apat/templates', static_folder='nrse_apat/static')

    app.config.from_object(config[environment])
    app.config.from_envvar('envvar_config', silent=True)
    
    return app


def get_app(name, environment=None):
    app = create_app(name, environment)

    # initiate extentions
    database.db.init_app(app)
    auth.init_app(app)

    # Initiate extentions
    app.register_blueprint(homepage_blueprint, url_prefix='/home')
    app.register_blueprint(actions_blueprint, url_prefix='/actions')
    app.register_blueprint(initiatives_blueprint, url_prefix='/initiatives')

    @app.route('/')
    @login_required
    def index():
        return redirect(url_for('homepage_blueprint.index'))

    app.secret_key = app.config['SECRET_KEY']

    return app


if __name__ == '__main__':
    app = get_app(__name__)
    app.run(debug=app.config['APP_DEBUG'])