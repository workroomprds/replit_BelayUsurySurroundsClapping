from src.oddEven2 import oddEven
import pytest


def test_oddEven():
	assert "even" == oddEven(2)
	assert "odd" == oddEven(1)
	assert "not an integer" == oddEven(0.1)
	assert "not a number" == oddEven("A")
	assert "empty input" == oddEven()