from src.oddEven import oddEven
import pytest


def test_oddEven_bad_method():
	with pytest.raises(ValueError):
		oddEven("")
