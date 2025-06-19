#!/usr/bin/python3
'''script that starts a flask application'''

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    states_list = []

    states = storage.all(State)

    for state in states.values():
        states_list.append({
            'id': state.id,
            'name': state.name,
            #'cities': [{'id': city.id, 'name': city.name} for city in state.cities]
        })

    return render_template('9-states.html', states=states_list, id=None)

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    states = storage.all(State)

    for state in states.values():
        if state.id == id:
            state_data = {
                'name': state.name,
                'cities': [{'id': city.id, 'name':city.name} for city in state.cities]
            }
            return render_template('9-states.html', state=state_data, id=id)

    return render_template('not_found.html'), 404

@app.teardown_appcontext
def teardown(exception):
    '''remove the current sqlalchemy session'''
    if exception:
        print(f"{exception}")
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
