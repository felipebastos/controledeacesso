from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
loginmanager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '123456'

    db.init_app(app)
    loginmanager.init_app(app)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
        from . import sohprausuarios
        app.register_blueprint(sohprausuarios.bp)

    return app