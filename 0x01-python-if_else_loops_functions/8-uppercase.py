#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        asci = ord(str[a])
        if asci >= 97 and asci <= 122:
            asci -= 32
        print("{0}".format(chr(asci)), end='')
    print("")
