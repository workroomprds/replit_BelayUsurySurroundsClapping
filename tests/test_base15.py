# -*- coding: utf-8 -*-
import unittest
from src import base15

subject = base15.Base15()


def test_availableCalls():
	assert callable(getattr(subject, "convertDecimalToBase15", None))
