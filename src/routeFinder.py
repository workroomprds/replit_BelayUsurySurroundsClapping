#!/usr/bin/env python3

from typing import List, Tuple, Optional, Union
from dataclasses import dataclass

@dataclass
class Point2Point:
    start: str
    end: str
    distance: float = 1
    duration: float = 60

    @property
    def step(self) -> Tuple[str, str]:
        return (self.start, self.end)

def makep2p(start: str, end: Optional[str] = None, distance: Optional[float] = None, duration: Optional[float] = None) -> Union[str, Point2Point]:
    if not start or not end:
        return "ERROR: no routes supplied to makep2p"
    return Point2Point(start, end, distance or 1, duration or 60)

@dataclass
class Route:
    path: List[Point2Point]

    @property
    def route(self) -> List[str]:
        return [p.start for p in self.path] + [self.path[-1].end]

    @property
    def distance(self) -> float:
        return sum(p.distance for p in self.path)

    @property
    def duration(self) -> float:
        return sum(p.duration for p in self.path)

@dataclass
class RouteResult:
    all_routes: List[Route]

    @property
    def allRoutes(self) -> List[List[str]]:
        return [route.route for route in self.all_routes]

    def _min_route(self, key_func):
        return min(self.all_routes, key=key_func) if self.all_routes else None

    @property
    def shortestRoute(self) -> Optional[Route]:
        return self._min_route(lambda r: r.distance)

    @property
    def fewestStops(self) -> Optional[Route]:
        return self._min_route(lambda r: len(r.route))

    @property
    def minDistance(self) -> Optional[Route]:
        return self.shortestRoute

    @property
    def minDuration(self) -> Optional[Route]:
        return self._min_route(lambda r: r.duration)

def create_route_map(routes: List[Union[Point2Point, Tuple[str, str]]]) -> Tuple[set, dict]:
    all_points = set()
    route_map = {}

    for route in routes:
        if isinstance(route, Point2Point):
            p2p = route
        elif isinstance(route, tuple):
            p2p = Point2Point(route[0], route[1])
        else:
            raise ValueError("Invalid route type")
        
        all_points.update(p2p.step)
        route_map.setdefault(p2p.start, []).append(p2p)
        route_map.setdefault(p2p.end, []).append(Point2Point(p2p.end, p2p.start, p2p.distance, p2p.duration))

    return all_points, route_map

def dfs(start: str, end: str, route_map: dict) -> List[List[Point2Point]]:
    def dfs_recursive(current: str, path: List[Point2Point], visited: set):
        if current == end:
            yield path
        for route in route_map.get(current, []):
            next_point = route.end
            if next_point not in visited:
                yield from dfs_recursive(next_point, path + [route], visited | {next_point})

    return list(dfs_recursive(start, [], {start}))

def findRoute(routes: List[Union[Point2Point, Tuple[str, str]]], start: str, end: str) -> Union[str, RouteResult]:
    if not routes:
        return "ERROR: no routes supplied"
    
    all_points, route_map = create_route_map(routes)

    if start not in all_points:
        return "ERROR: start point is not in routes"
    if end not in all_points:
        return "ERROR: end point is not in routes"

    all_routes = dfs(start, end, route_map)
    valid_routes = [Route(route) for route in all_routes if route[-1].end == end]
    
    if not valid_routes:
        return "ERROR: there is no connection between start and end"
    
    return RouteResult(valid_routes)

__all__ = ['findRoute', 'makep2p']
