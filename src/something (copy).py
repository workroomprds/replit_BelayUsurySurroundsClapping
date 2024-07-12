#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Something:
    def __init__(self):
        pass

    def newThing(self, param=None):
        if param is None:
            return "nothing supplied"
        elif param == 2:
            return "4"
        elif isinstance(param, int):
            return str(param ** 2)
        elif param == "Jim":
            return "Gentleman Jim"
        elif isinstance(param, list):
            if param == ["stop", "start"]:
                return "you must stop before you can start"
            elif param == ["give", "take"]:
                return "you must give before you can take"
            elif len(param) == 2:
                return f"you must {param[0]} before you can {param[1]}"
        return str(param)

# This line is added to ensure the Something class is accessible when imported
__all__ = ['Something']
