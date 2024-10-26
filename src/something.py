#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Something:
    def newThing(self, input=None):
        if input is None:
            return "nothing supplied"
        elif isinstance(input, int):
            return str(input ** 2)
        elif isinstance(input, str):
            if input == "Jim":
                return "Gentleman Jim"
            else:
                return input
        elif isinstance(input, list) and len(input) == 2:
            if input == ["stop", "start"]:
                return "you must stop before you can start"
            elif input == ["give", "take"]:
                return "you must give before you can take"
            else:
                return f"you must {input[0]} before you can {input[1]}"
        else:
            return str(input)

# This line is needed to make the Something class available when imported
__all__ = ['Something']
