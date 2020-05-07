#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list[:]
    for index, i in enumerate(my_list):
        if i == search:
            my_list[index] = replace
    return my_list
