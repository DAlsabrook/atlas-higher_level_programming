#!/usr/bin/python
def roman_to_int(roman_string):
    #if not isinstance(roman_string, str) or roman_string is None:
    #    return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_num = 0

    for char in reversed(roman_string):
        num = roman_numerals.get(char, 0)

        if prev_num > num:
            result -= num
        else:
            result += num

        prev_num = num
    return result
        
