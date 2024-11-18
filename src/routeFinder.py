#!/usr/bin/env python3

def findRoute(routes, start, end):
    for route in routes:
        if route == (start, end):
            return [start, end]
        elif route == (end, start):
            return [start, end]
    return None
