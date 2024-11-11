from src.oddEven import oddEven
import pytest

odd = [
	1, 31, 55, -1, 257
]

@pytest.mark.parametrize("candidate", odd)
def test_oddEven(candidate):
	assert "odd" == oddEven(candidate)



def test_oddEven_bad_method():
	with pytest.raises(ValueError):
		oddEven("")
