# -*- coding: utf-8 -*-
import unittest
from src import frogs

def setup_function(function):
	subject = frogs.Frogs()


def test_availableCalls():
	subject = frogs.Frogs()
	assert callable(getattr(subject, "newFrog", None))
	assert callable(getattr(subject, "getFrogs", None))
	assert callable(getattr(subject, "countFrogs", None))
	assert callable(getattr(subject, "findFrog", None))

def test_getFrogs():
	subject = frogs.Frogs()
	assert subject.getFrogs() == []

def test_newFrog():
	subject = frogs.Frogs()
	assert subject.getFrogs() == []
	testFrog = {"name": "frog1"}
	subject.newFrog(testFrog)
	assert len(subject.getFrogs()) == 1

def test_countFrogs():
	subject = frogs.Frogs()
	assert subject.getFrogs() == []
	testFrog = {"name": "frog1"}
	subject.newFrog(testFrog)
	assert subject.countFrogs() == 1