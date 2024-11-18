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
                    return new_path
                result = dfs(next_point, new_path)
                if result:
                    return result
        
        return None

    result = dfs(start, [start])
    if result:
        return [result] if len(result) == 2 else [result]
    return None
