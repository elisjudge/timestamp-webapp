from flask import Flask
from config import Config
from routes import routes

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration

    # Register Blueprints
    app.register_blueprint(routes)

    return app
