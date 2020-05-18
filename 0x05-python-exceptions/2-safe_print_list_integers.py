#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            indx += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print("")
    return indx
