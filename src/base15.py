#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Base15:
    def __init__(self):
        self.digits = "0123456789ABCDE"

    def convertDecimalToBase15(self, decimal):
        if decimal == 0:
            return "0"
        
        result = ""
        while decimal > 0:
            remainder = decimal % 15
            result = self.digits[remainder] + result
            decimal //= 15
        
        return result

# Remove this line as it's causing the error
# Base15 = Base15()
