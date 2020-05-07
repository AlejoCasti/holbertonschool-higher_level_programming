#!/usr/bin/python3
def best_score(a_dictionary):
    max_key = None
    if a_dictionary:
        max_va = max(list(a_dictionary.values()))
        max_key = [i for i in a_dictionary if a_dictionary[i] == max_va][0]
    return max_key
