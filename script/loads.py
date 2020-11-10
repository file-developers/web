# This file is used to store all the functions that load a json
# file to a Python structure using the JSON module.
import json

def load_errors():
    """
    This function loads the error.json file to get all the HTTP
    errors to a Python dic.

    returns: The file itself using the json module
    """
    ROUTE = 'static/json/errors.json'
    with open(ROUTE, 'r') as f:
        # load and return the actual route
        return json.load(f)
