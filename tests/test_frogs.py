# -*- coding: utf-8 -*-
import unittest
from src import frogs

subject = frogs.Frogs()


def test_availableCalls():
	assert callable(getattr(subject, "newFrog", None))
