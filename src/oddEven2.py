#!/usr/bin/env python3

def oddEven(number):
    if not isinstance(number, (int, float)):
        return "not a number"
    if not isinstance(number, int):
        return "not an integer"
    elif number % 2 == 0:
        return "even"
    else:
        return "odd"
