#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    print("{0}".format(number % 10), end='')
    return number % 10
