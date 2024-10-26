# -*- coding: utf-8 -*-
import unittest, pytest
from src import frogs


@pytest.fixture
def subject():
	return frogs.Frogs()


def test_availableCalls(subject):
	assert callable(getattr(subject, "newFrog", None))
	assert callable(getattr(subject, "getFrogs", None))
	assert callable(getattr(subject, "findFirstFrogByName", None))
	assert callable(getattr(subject, "findIndexOfFirstFrogByName", None))
	assert callable(getattr(subject, "getFrogByIndex", None))
	assert callable(getattr(subject, "getFrogByName", None))

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


def test_findFirstFrogByName(subject):
	testFrog1 = {"name": "frog1"}
	subject.newFrog(testFrog1)
	testFrog2 = {"name": "frog1"}
	subject.newFrog(testFrog2)
	testFrog3 = {"name": "frog3"}
	subject.newFrog(testFrog3)
	assert subject.findFirstFrogByName("frog3") == 2


def test_getFrogByName(subject):
	testFrog1 = {"name": "frog1"}
	subject.newFrog(testFrog1)
	testFrog2 = {"name": "frog2"}
	subject.newFrog(testFrog2)
	testFrog3 = {"name": "frog3"}
	subject.newFrog(testFrog3)
	assert subject.getFrogByName("frog2") == testFrog2
