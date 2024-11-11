from src.bucketise import bucketise
import pytest


def test_easter_bad_method():
	with pytest.raises(ValueError):
		bucketise("")
