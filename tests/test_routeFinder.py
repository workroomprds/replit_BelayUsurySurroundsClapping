from src.routeFinder import findRoute, makep2p
import pytest


def test_routeFinder():
	assert callable(findRoute)
	assert callable(makep2p)


def test_makep2p():
	assert ("A", "B") == makep2p("A", "B", 5, 10).step
	assert 5 == makep2p("A", "B", 5, 10).distance
	assert 10 == makep2p("A", "B", 5, 10).duration
	#default distance
	assert 1 == makep2p("A", "B", None, 10).distance
	#default duration
	assert 60 == makep2p("A", "B", 5, None).duration


def test_two_point_route():  #should return a list of lists
	routes = [makep2p("A", "B"), makep2p("B", "C")]
	assert findRoute(routes, "A", "B").allRoutes == [["A", "B"]]
	assert findRoute(routes, "B", "A").allRoutes == [["B", "A"]]
	assert findRoute(routes, "B", "C").allRoutes == [["B", "C"]]


def test_three_point_route():
	routes = [makep2p("A", "B"), makep2p("B", "C")]
	assert findRoute(routes, "A", "C").allRoutes == [["A", "B", "C"]]
	assert findRoute(routes, "C", "A").allRoutes == [["C", "B", "A"]]


def test_route_offers_alternatives():
	routes = [makep2p("A", "B"), makep2p("B", "C"), makep2p("A", "C")]
	assert len(findRoute(routes, "A", "C").allRoutes) == 2
	assert ["A", "C"] in findRoute(routes, "A", "C").allRoutes
	assert ["A", "B", "C"] in findRoute(routes, "A", "C").allRoutes
	#the route with the smallest aggregate distance
	assert ["A", "C"] == findRoute(routes, "A", "C").fewestStops.route

def test_calculates_distance():
	routes = [makep2p("A", "B", 2, 20), makep2p("B", "C", 3, 30)]
	assert ["A", "B", "C"] == findRoute(routes, "A", "C").fewestStops.route
	assert 5 == findRoute(routes, "A", "C").fewestStops.distance

def test_calculates_duration():
	routes = [makep2p("A", "B", 2, 40), makep2p("B", "C", 3, 30)]
	assert ["A", "B", "C"] == findRoute(routes, "A", "C").fewestStops.route
	assert 70 == findRoute(routes, "A", "C").fewestStops.duration

def test_longer_route():
	routes = [
	    makep2p("A", "B"),
	    makep2p("B", "C"),
	    makep2p("A", "C"),
	    makep2p("C", "D"),
	    makep2p("D", "E"),
	    makep2p("E", "F")
	]
	assert ["A", "C", "D", "E", "F"] in findRoute(routes, "A", "F").allRoutes


def test_errors():
	assert findRoute(None, "A", "B") == "ERROR: no routes supplied"
	assert findRoute([], "A", "B") == "ERROR: no routes supplied"
	assert findRoute([makep2p("A", "B")], "C",
	                 "B") == "ERROR: start point is not in routes"
	assert findRoute([makep2p("A", "B")], "A",
	                 "C") == "ERROR: end point is not in routes"
	assert findRoute(
	    [("A", "B"), ("C", "D")], "A",
	    "D") == "ERROR: there is no connection between start and end"
