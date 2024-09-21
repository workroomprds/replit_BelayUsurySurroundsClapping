#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frogs:
    def __init__(self):
        self.frogs = []

    def newFrog(self, frog):
        self.frogs.append(frog)

    def getFrogs(self):
        return self.frogs

if __name__ == "__main__":
    frogs = Frogs()
