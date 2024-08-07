from flask import Flask
from flask_pymongo import PyMongo
from .config import Config
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    with app.app_context():
        from .Routes import admin_routes
        app.register_blueprint(admin_routes.app)   
       
        return app