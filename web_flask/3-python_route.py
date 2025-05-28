#!/usr/bin/python3
'''script that starts a flask application'''

from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def displayc(text):
    display = "C " + text.replace('_', ' ')
    return display

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displaypython(text="is cool"):
    display = "Python " + text.replace('_', ' ')
    return display


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
