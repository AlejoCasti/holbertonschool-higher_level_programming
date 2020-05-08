#!/usr/bin/python3
def roman_to_int(roman_string):
    suma, current, nexto = 0, 0, 0
    letter = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
              'D': 500, 'M': 1000}
    if type(roman_string) != str:
        return None
    for idx, i in enumerate(roman_string):
        current = letter.get(i)
        if idx < len(roman_string) - 1:
            nexto = letter.get(roman_string[idx + 1])
            if current >= nexto:
                suma += current
            else:
                suma -= current
        else:
            suma += current
    return suma
