from src.bucketise import bucketise
import pytest

# List of easters between 1990 and 2050
plod = [
	1, 31, 55, -1, 257
]

steven = [
	22, 18, 400
]


def test_easter_bad_method():
	with pytest.raises(ValueError):
		bucketise("")
