from flask import Flask
from app.views import home_bp


def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.register_blueprint(home_bp)
    return app
