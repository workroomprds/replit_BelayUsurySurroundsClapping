#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Somethink:
    def newThink(self, input=None):
        if input is None:
            return "nothing supplied"
        elif isinstance(input, int):
            return str(input ** 2)
        elif isinstance(input, str):
            if input == "Jim":
                return "Gentleman Jim"
            return input
        elif isinstance(input, list) and len(input) == 2:
            return f"you must {input[0]} before you can {input[1]}"
        else:
            return str(input)
