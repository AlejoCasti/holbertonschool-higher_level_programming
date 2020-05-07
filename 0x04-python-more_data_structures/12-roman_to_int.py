#!/usr/bin/python3
def roman_to_int(roman_string):
    suma = 0
    if type(roman_string) != str:
        return None
    for i in roman_string:
        suma += 1 if i == 'I' else 0
        suma += 5 if i == 'V' else 0
        suma += 10 if i == 'X' else 0
        suma += 50 if i == 'L' else 0
        suma += 100 if i == 'C' else 0
        suma += 500 if i == 'D' else 0
        suma += 1000 if i == 'M' else 0
    return suma
