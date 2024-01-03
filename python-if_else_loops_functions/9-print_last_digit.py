#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    num %= 10
    if number < 0:
        num = -num
    return num
