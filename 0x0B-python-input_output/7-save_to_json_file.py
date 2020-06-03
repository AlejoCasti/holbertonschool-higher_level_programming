#!/usr/bin/python3
""" Read a file named as filename """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w+') as fil:
        json.dump(my_obj, fil)
