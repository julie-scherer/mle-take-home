from flask import Flask


# Instantiate Flask application factory
app = Flask(__name__)


# Register the API blueprint to the app factory function
from app.api import bp
app.register_blueprint(bp)




