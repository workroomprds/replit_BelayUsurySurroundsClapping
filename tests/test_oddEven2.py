import pytest
from src.oddEven2 import oddEven

expected_even = [2, 0, -4, 100, 1000]
expected_odd = [1, -3, 5, 99, 1001, "1"]  # Including "1" here

@pytest.mark.parametrize("number", expected_even)
def test_even_numbers(number):
		assert "even" == oddEven(number)

@pytest.mark.parametrize("number", expected_odd)
def test_odd_numbers(number):
		assert "odd" == oddEven(number)

@pytest.mark.parametrize("input_value, expected_output", [
		(0.1, "not an integer"),
		("A", "not a number"),
		("", "empty input"),
		(None, "empty input"),
])
def test_special_cases(input_value, expected_output):
		assert expected_output == oddEven(input_value)

def test_oddEven_no_argument():
		assert "empty input" == oddEven()