# -*- coding: utf-8 -*-
import unittest
from src import something

subject = something.Something()


def test_availableCalls():
	assert callable(getattr(subject, "newThing", None))


def test_newThing():
	#assert subject.newThing() == "nothing supplied"
	#assert subject.newThing(1) == "1"
	#assert subject.newThing(2) == "4"
	#assert subject.newThing(3) == "9"
	#assert subject.newThing(4) == "16"
	#assert subject.newThing("bob") == "bob"
	assert subject.newThing("Jim") == "Gentleman Jack"
	assert subject.newThing("Jim") == "Gentleman Jim" 
	#assert subject.newThing(["stop", "start"]) == "you must stop before you can start"
	#assert subject.newThing(["give", "take"]) == "you must give before you can take"
	#assert subject.newThing(["1", "2"]) == "you must 1 before you can 2"