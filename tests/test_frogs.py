# -*- coding: utf-8 -*-
import unittest, pytest
from src import frogs

@pytest.fixture
def subject():
		return frogs.Frogs()

def test_availableCalls(subject):
	assert callable(getattr(subject, "newFrog", None))
	assert callable(getattr(subject, "getFrogs", None))
