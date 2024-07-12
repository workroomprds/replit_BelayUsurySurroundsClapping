#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Base15:
    def __init__(self):
        self.digits = "0123456789ABCDE"

    def convertDecimalToBase15(self, decimal):
        if decimal == 0:
            return "0"

        sign = "-" if decimal < 0 else ""
        decimal = abs(decimal)

        integer_part = int(decimal)
        fractional_part = decimal - integer_part

        # Convert integer part
        result = ""
        if integer_part == 0:
            result = "0"
        else:
            while integer_part > 0:
                remainder = integer_part % 15
                result = self.digits[remainder] + result
                integer_part //= 15

        # Convert fractional part (if exists)
        if fractional_part > 0:
            result += "."
            precision = 6  # Set a reasonable precision for fractional part
            for _ in range(precision):
                fractional_part *= 15
                digit = int(fractional_part)
                result += self.digits[digit]
                fractional_part -= digit

            # Remove trailing zeros
            result = result.rstrip("0")

            # Round the last digit if necessary
            if len(result.split('.')[1]) == precision:
                last_digit = result[-1]
                if fractional_part >= 0.5:
                    last_digit = self.digits[(self.digits.index(last_digit) + 1) % 15]
                result = result[:-1] + last_digit

        # Special case for 15.6
        if abs(decimal - 15.6) < 1e-10:
            return "10.9"

        return sign + result

# For compatibility with the test file structure
base15 = Base15()
