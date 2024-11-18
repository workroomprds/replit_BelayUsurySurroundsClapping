#!/usr/bin/env python3

def findRoute(routes, start, end):
    if not routes:
        return "ERROR: no routes supplied"
    
    all_points = set()
    for route in routes:
        all_points.update(route)
    
    if start not in all_points:
        return "ERROR: start point is not in routes"
    if end not in all_points:
        return "ERROR: end point is not in routes"

    def dfs(current, path):
        if current == end:
            yield path
        for route in routes:
            next_point = None
            if route[0] == current:
                next_point = route[1]
            elif route[1] == current:
                next_point = route[0]
            
            if next_point and next_point not in path:
                new_path = path + [next_point]
                yield from dfs(next_point, new_path)

    all_routes = list(dfs(start, [start]))
    return [route for route in all_routes if route[-1] == end]
