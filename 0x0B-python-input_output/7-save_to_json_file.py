#!/usr/bin/python3
""" JSON project """
import json


def save_to_json_file(my_obj, filename):
    """ save to JSON file """
    with open(filename, 'w+') as fil:
        json.dump(my_obj, fil)
