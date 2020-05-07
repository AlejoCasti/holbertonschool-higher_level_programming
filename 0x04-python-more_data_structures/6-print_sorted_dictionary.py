#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_di = sorted(a_dictionary.keys())
    for j in a_di:
        print("{}: {}".format(j, a_dictionary[j]))
