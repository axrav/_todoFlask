from flask import Flask
import os
from api_blueprint import api
from gunicorn import glogging
app = Flask(__name__)


# custom error handler
@app.errorhandler(404)
def not_found(e):
    return {"error": "404 Not Found"}

# /api blueprint for todo api's
app.register_blueprint(api)





