#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Base15:
    def __init__(self):
        self.digits = "0123456789ABCDE"

    def convertDecimalToBase15(self, decimal):
        if isinstance(decimal, int):
            return self._convert_integer(decimal)
        elif isinstance(decimal, float):
            return self._convert_float(decimal)
        else:
            raise ValueError("Input must be an integer or float")

    def _convert_integer(self, decimal):
        if decimal == 0:
            return "0"
        
        is_negative = decimal < 0
        decimal = abs(decimal)
        
        result = ""
        while decimal > 0:
            remainder = decimal % 15
            result = self.digits[remainder] + result
            decimal //= 15
        
        if is_negative:
            result = "-" + result
        
        return result

    def _convert_float(self, decimal):
        integer_part = int(decimal)
        fractional_part = abs(decimal - integer_part)

        integer_result = self._convert_integer(integer_part)

        if fractional_part == 0:
            return integer_result

        fractional_result = "."
        precision = 6
        
        for _ in range(precision):
            fractional_part *= 15
            digit = int(fractional_part)
            fractional_result += self.digits[digit]
            fractional_part -= digit

        # Round the fractional part
        fractional_result = fractional_result.rstrip("0")
        if len(fractional_result) > 1:
            rounded, carry = self._round_fractional(fractional_result[1:])
            if carry:
                integer_result = self._convert_integer(int(integer_result) + 1)
            fractional_result = "." + rounded

        # Remove trailing dot if there are no decimal places
        if fractional_result == ".":
            return integer_result
        
        return integer_result + fractional_result

    def _round_fractional(self, fractional):
        rounded = ""
        carry = 0
        for digit in reversed(fractional):
            value = self.digits.index(digit) + carry
            if value >= 15:
                carry = 1
                value -= 15
            else:
                carry = 0
            rounded = self.digits[value] + rounded
        
        # Check if we need to round up
        if len(rounded) > 0 and self.digits.index(rounded[0]) >= 8:
            return self._round_fractional("1" + rounded)[0], 1
        
        return rounded.rstrip("0"), carry
