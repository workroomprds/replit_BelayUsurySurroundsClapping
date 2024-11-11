from src.oddEven import oddEven
import pytest

odd = [
	1, 31, 55, -1, 257, "1", 5.9, "-11", "-11.001"
]

@pytest.mark.parametrize("candidate", odd)
def test_oddEven(candidate):
	assert "odd" == oddEven(candidate)

even = [
	22, 18, 400, "2", "100.01"
]

@pytest.mark.parametrize("candidate", even)
def test_oddEven(candidate):
	assert "even" == oddEven(candidate)

def test_oddEven_bad_method():
	with pytest.raises(ValueError):
		oddEven("")
