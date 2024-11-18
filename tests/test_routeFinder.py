from src.routeFinder import findRoute	
import pytest


def test_routeFinder():
	assert callable(findRoute)
	
def test_two_point_route(): #should return a list of lists
	routes = [("A", "B"), ("B", "C")]
	assert findRoute(routes, "A", "B") == [["A", "B"]]
	assert findRoute(routes, "B", "A") == [["B", "A"]]
	assert findRoute(routes, "B", "C") == [["B", "C"]]


def test_three_point_route():
	routes = [("A", "B"), ("B", "C")]
	assert findRoute(routes, "A", "C") == [["A", "B", "C"]]
	assert findRoute(routes, "C", "A") == [["C", "B", "A"]]

def test_route_offers_alternatives():
	routes = [("A", "B"), ("B", "C"), ["A", "C"]]
	assert len(findRoute(routes, "A", "C")) == 2
	assert ["A", "C"] in findRoute(routes, "A", "C")
	assert ["A", "B", "C"] in findRoute(routes, "A", "C")


