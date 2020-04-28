#!/usr/bin/python3
letter = 97
for i in range(26):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print(chr(letter), end = '')
    letter += 1
