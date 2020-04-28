#!/usr/bin/python3
def uppercase(str):
    if str is not None:
        for a in range(len(str)):
            asci = ord(str[a])
            if asci >= 97 and asci <= 122:
                asci -= 32
            if a == len(str) - 1:
                print(chr(asci))
            else:
                print("{0}".format(chr(asci)), end='')
