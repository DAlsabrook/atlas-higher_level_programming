#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        print("Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i, end=" ")
