#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Something:
    def newThing(self, arg=None):
        if arg is None:
            return "nothing supplied"
        elif isinstance(arg, int):
            return str(arg ** 2)
        elif isinstance(arg, str):
            if arg == "Jim":
                return "Gentleman Jim"
            return arg
        elif isinstance(arg, list) and len(arg) == 2:
            return f"you must {arg[0]} before you can {arg[1]}"
        else:
            return str(arg)

# This line is needed to make the Something class available when imported
something = Something()
