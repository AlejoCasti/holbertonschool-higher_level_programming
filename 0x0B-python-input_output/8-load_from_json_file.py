#!/usr/bin/python3
""" JSON project """
import json


def load_from_json_file(filename):
    """ Load form JSON file """
    with open(filename, 'r') as fil:
        return json.load(fil)
