from src.routeFinder import findRoute	
import pytest


def test_routeFinder():
	assert callable(findRoute)
