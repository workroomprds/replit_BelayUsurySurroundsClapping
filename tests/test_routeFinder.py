from src.routeFinder import findRoute	
import pytest


def test_routeFinder():
	assert callable(findRoute)
	
def test_two_point_route():
	routes = [("A", "B")]
	assert findRoute(routes, "A", "B") == ["A", "B"]
	assert findRoute(routes, "B", "A") == ["B", "A"]
		


