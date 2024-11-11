#!/usr/bin/env python3

def oddEven(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number")
    
    if isinstance(number, float):
        number = int(number)
    
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
