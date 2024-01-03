#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = abs(number)
    num %= 10
    if number < 0:
        num = -abs(num)
    return num
