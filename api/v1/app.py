#!/usr/bin/python3
'''An instance of app'''

import os
from flask import Flask, jsonify
from models import storage
from flask_cors import CORS
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, origins="0.0.0.0")


@app.errorhandler(404)
def handle_404(error):
    '''handler for 404 errors'''
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def close_connection(exc):
    '''calls storage.close'''
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)
