#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    value = 0
    try:
        for idx, i in enumerate(my_list):
            if idx < x:
                value = idx + 1
                print("{}".format(i), end='')
        print("")
    except ValueError:
        print("it cannot print")
    return value
