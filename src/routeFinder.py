#!/usr/bin/env python3

class Point2Point:
    def __init__(self, start, end, distance=None, duration=None):
        self.step = (start, end)
        self.distance = 1 if distance is None else distance
        self.duration = 60 if duration is None else duration

def makep2p(start, end, distance=None, duration=None):
    return Point2Point(start, end, distance, duration)

class Route:
    def __init__(self, path):
        self.route = [p.step[0] for p in path] + [path[-1].step[1]]
        self.distance = sum(p.distance for p in path)
        self.duration = sum(p.duration for p in path)

class RouteResult:
    def __init__(self, all_routes):
        self.allRoutes = [route.route for route in all_routes]
        self.shortestRoute = min(all_routes, key=lambda r: r.distance) if all_routes else None
        self.fewestStops = min(all_routes, key=lambda r: len(r.route)) if all_routes else None

def findRoute(routes, start, end):
    if not routes:
        return "ERROR: no routes supplied"
    
    all_points = set()
    route_map = {}
    for route in routes:
        if isinstance(route, Point2Point):
            all_points.update(route.step)
            route_map.setdefault(route.step[0], []).append(route)
            route_map.setdefault(route.step[1], []).append(Point2Point(route.step[1], route.step[0], route.distance, route.duration))
        elif isinstance(route, tuple):
            all_points.update(route)
            p2p = Point2Point(route[0], route[1])
            route_map.setdefault(route[0], []).append(p2p)
            route_map.setdefault(route[1], []).append(Point2Point(route[1], route[0]))
        else:
            raise ValueError("Invalid route type")
    
    if start not in all_points:
        return "ERROR: start point is not in routes"
    if end not in all_points:
        return "ERROR: end point is not in routes"

    def dfs(current, path, visited):
        if current == end:
            yield path
        for route in route_map.get(current, []):
            next_point = route.step[1]
            if next_point not in visited:
                yield from dfs(next_point, path + [route], visited | {next_point})

    all_routes = list(dfs(start, [], {start}))
    valid_routes = [Route(route) for route in all_routes if route[-1].step[1] == end]
    
    if not valid_routes:
        return "ERROR: there is no connection between start and end"
    
    return RouteResult(valid_routes)

__all__ = ['findRoute', 'makep2p']
