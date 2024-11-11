#!/usr/bin/env python3

def oddEven(number):
    if isinstance(number, str):
        try:
            number = int(number)
        except ValueError:
            raise ValueError("Input must be a number or a string representation of a number")
    elif not isinstance(number, (int, float)):
        raise ValueError("Input must be a number or a string representation of a number")
    
    if isinstance(number, float):
        number = int(number)
    
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
