from src.oddEven2 import oddEven
import pytest


def test_oddEven():
	assert "even" == oddEven(2)
	assert "odd" == oddEven(1)