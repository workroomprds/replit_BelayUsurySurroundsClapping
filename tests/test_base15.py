# -*- coding: utf-8 -*-
import unittest
from src import base15

subject = base15.Base15()


def test_availableCalls():
	assert callable(getattr(subject, "convertDecimalToBase15", None))


def test_convertDecimalToBase15():
	assert subject.convertDecimalToBase15(1) == "1"
	assert subject.convertDecimalToBase15(0) == "0"
	assert subject.convertDecimalToBase15(10) == "A"
	assert subject.convertDecimalToBase15(15) == "10"
	assert subject.convertDecimalToBase15(16) == "11"
	assert subject.convertDecimalToBase15(150) == "A0"
	assert subject.convertDecimalToBase15(-1) == "-1"
	assert subject.convertDecimalToBase15(-225) == "-100"


assert subject.convertDecimalToBase15(15.6) == "10.9"
assert subject.convertDecimalToBase15(14.8) == "E.C"
assert subject.convertDecimalToBase15(14.888) == "E.D4C"

