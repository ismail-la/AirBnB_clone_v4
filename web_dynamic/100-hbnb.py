#!/usr/bin/python3
""" Script that starts a Flash Web Application """

import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template


app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """
    This function will be called when the Flask app context tears down.
    It closes the database session
    """
    storage.close()


@app.route('/100-hbnb/', strict_slashes=False)
def hbnb():
    """
    Defines a route for the web application.
    When a user visits the ‘/100-hbnb/’ URL path, the hbnb function is called.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())


if __name__ == "__main__":
    """
    If this script is run directly (not imported as a module),
    it starts the Flask development server on the host ‘0.0.0.0’ and port 5001.
    """
    app.run(host='0.0.0.0', port=5001)
