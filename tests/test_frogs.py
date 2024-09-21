# -*- coding: utf-8 -*-
import unittest
from src import frogs

subject = frogs.Frogs()


def test_availableCalls():
	assert callable(getattr(subject, "newFrog", None))
	assert callable(getattr(subject, "getFrogs", None))

def test_getFrogs():
	assert subject.getFrogs() == []

def test_newFrog():
	assert subject.getFrogs() == []
	testFrog = {"name": "frog1"}
	subject.newFrog(testFrog)
	assert len(subject.getFrogs()) == 1