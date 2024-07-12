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
        precision = 6  # Number of decimal places to calculate
        
        for _ in range(precision):
            fractional_part *= 15
            digit = int(fractional_part)
            fractional_result += self.digits[digit]
            fractional_part -= digit

        # Round the last digit
        if fractional_part >= 0.5:
            last_digit = self.digits.index(fractional_result[-1])
            if last_digit == 14:  # If the last digit is 'E'
                fractional_result = fractional_result[:-1] + '0'
                # Propagate carry
                for i in range(len(fractional_result) - 2, 0, -1):
                    if fractional_result[i] == 'E':
                        fractional_result = fractional_result[:i] + '0' + fractional_result[i+1:]
                    else:
                        next_digit = self.digits[self.digits.index(fractional_result[i]) + 1]
                        fractional_result = fractional_result[:i] + next_digit + fractional_result[i+1:]
                        break
                else:
                    # If we've carried all the way to the integer part
                    integer_result = self._convert_integer(int(integer_result) + 1)
            else:
                fractional_result = fractional_result[:-1] + self.digits[last_digit + 1]

        # Remove trailing zeros
        fractional_result = fractional_result.rstrip("0")
        
        # Remove trailing dot if there are no decimal places
        if fractional_result == ".":
            return integer_result
        
        return integer_result + fractional_result
