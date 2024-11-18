#!/usr/bin/env python3

class Point2Point:
    def __init__(self, start, end):
        self.step = (start, end)

def makep2p(start, end):
    return Point2Point(start, end)

def findRoute(routes, start, end):
    if not routes:
        return "ERROR: no routes supplied"
    
    all_points = set()
    for route in routes:
        if isinstance(route, Point2Point):
            all_points.update(route.step)
        elif isinstance(route, tuple):
            all_points.update(route)
        else:
            raise ValueError("Invalid route type")
    
    if start not in all_points:
        return "ERROR: start point is not in routes"
    if end not in all_points:
        return "ERROR: end point is not in routes"

    def dfs(current, path):
        if current == end:
            yield path
        for route in routes:
            next_point = None
            if isinstance(route, Point2Point):
                step = route.step
            elif isinstance(route, tuple):
                step = route
            else:
                continue
            
            if step[0] == current:
                next_point = step[1]
            elif step[1] == current:
                next_point = step[0]
            
            if next_point and next_point not in path:
                new_path = path + [next_point]
                yield from dfs(next_point, new_path)

    all_routes = list(dfs(start, [start]))
    valid_routes = [route for route in all_routes if route[-1] == end]
    
    if not valid_routes:
        return "ERROR: there is no connection between start and end"
    
    return valid_routes

# The following line is added to make the functions importable
__all__ = ['findRoute', 'makep2p']
