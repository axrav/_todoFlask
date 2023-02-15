from flask import Flask
from api_blueprint import api
app = Flask(__name__)


# custom error handler
@app.errorhandler(404)
def not_found(e):
    return {"error": "404 Not Found"}

# /api blueprint for todo api's
app.register_blueprint(api)





