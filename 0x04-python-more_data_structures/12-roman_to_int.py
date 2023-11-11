#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = i = 0
        length = len(roman_string)
        while i < length:
            if i == length-1 or n[roman_string[i]] >= n[roman_string[i+1]]:
                res += n[roman_string[i]]
                i += 1
            else:
                res += n[roman_string[i+1]] - n[roman_string[i]]
                i += 2
        return res
    else:
        return 0
