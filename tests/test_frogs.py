# -*- coding: utf-8 -*-
import unittest, pytest
from src import frogs

@pytest.fixture
def subject():
		return frogs.Frogs()

def test_availableCalls(subject):
	assert callable(getattr(subject, "newFrog", None))
	assert callable(getattr(subject, "getFrogs", None))

def test_getFrogs(subject):
	assert subject.getFrogs() == []

def test_newFrog(subject):
	assert subject.getFrogs() == []
	testFrog = {"name": "frog1"}
	subject.newFrog(testFrog)
	assert len(subject.getFrogs()) == 1

def test_countFrogs(subject):
	assert subject.getFrogs() == []
	testFrog = {"name": "frog1"}
	subject.newFrog(testFrog)
	assert subject.countFrogs() == 1