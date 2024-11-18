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
                result = dfs(next_point, path + [next_point])
                if result:
                    return result
        
        return None

    return dfs(start, [start])
