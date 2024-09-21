#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frogs:
    def __init__(self):
        self.frogs = []

    def newFrog(self, frog):
        self.frogs.append(frog)

    def getFrogs(self):
        return self.frogs

    def countFrogs(self):
        return len(self.frogs)

    def findFrog(self, name):
        for frog in self.frogs:
            if frog.get('name') == name:
                return frog
        return None
