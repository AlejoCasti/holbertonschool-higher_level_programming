#!/usr/bin/python3
""" Read a file named as filename """
import json


def from_json_string(my_str):
    return json.loads(my_str)
