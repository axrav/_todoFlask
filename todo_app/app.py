from flask import Flask

from api_blueprint import api

app = Flask(__name__)

# /api blueprint for todo api's
app.register_blueprint(api)
