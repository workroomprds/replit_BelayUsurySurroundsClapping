#!/usr/bin/env python3

def findRoute(routes, start, end):
    def dfs(current, path):
        if current == end:
            return path

        for route in routes:
            next_point = None
            if route[0] == current:
                next_point = route[1]
            elif route[1] == current:
                next_point = route[0]
            
            if next_point and next_point not in path:
                new_path = path + [next_point]
                if next_point == end:
                    yield new_path
                else:
                    yield from dfs(next_point, new_path)

    all_routes = list(dfs(start, [start]))
    if all_routes:
        return [route for route in all_routes if route[-1] == end]
    return None
