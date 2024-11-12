#!/usr/bin/env python3

def oddEven(number=None):
    if number is None or number == "":
        return "empty input"
    
    if isinstance(number, str):
        try:
            number = int(number)
        except ValueError:
            return "not a number"
    
    if not isinstance(number, (int, float)):
        return "not a number"
    
    if not isinstance(number, int):
        return "not an integer"
    
    return "even" if number % 2 == 0 else "odd"
