#!/usr/bin/python3
""" Read a file named as filename """
import json


def load_from_json_file(filename):
    with open(filename, 'r') as fil:
        return json.load(fil)
