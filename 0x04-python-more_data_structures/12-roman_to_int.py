#!/usr/bin/python3
def roman_to_int(roman_string):
    suma, current, nexto = 0, 0, 0
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
              'D': 500, 'M': 1000}
    if type(roman_string) != str:
        return None
    for idx, i in enumerate(roman_string):
        if idx < len(roman_string):
            current = letter.get(i)
            nexto = letter.get(roman_string[idx])
            if current >= nexto:
                suma += current
            else:
                suma -= current
    return suma
