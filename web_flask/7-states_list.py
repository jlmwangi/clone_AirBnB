#!/usr/bin/python3
'''script that starts a flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    states_list = []
    states = storage.all(State)
#    print(states)

    for state in states.values():
        states_list.append({'id': state.id, 'name': state.name})

    return render_template('7-states_list.html', states=states_list)

@app.teardown_appcontext
def teardown(exception):
    '''remove the current sqlalchemy session'''
    if exception:
        print(f"{exception}")
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
