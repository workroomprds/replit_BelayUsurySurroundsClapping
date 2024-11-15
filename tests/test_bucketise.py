from src.bucketise import bucketise
import pytest

# List of easters between 1990 and 2050
plod = [
	1, 31, 55, -1, 257
]

steven = [
	22, 18, 400
]


@pytest.mark.parametrize("candidate", plod)
def test_bucketise(candidate):
	assert "plod" == bucketise(candidate)

@pytest.mark.parametrize("candidate", steven)
def test_bucketise(candidate):
	assert "steven" == bucketise(candidate)

def test_easter_bad_method():
	with pytest.raises(ValueError):
		bucketise("")
