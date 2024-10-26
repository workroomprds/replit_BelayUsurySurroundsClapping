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

    def findFirstFrogByName(self, name):
        for i, frog in enumerate(self.frogs):
            if frog.get('name') == name:
                return i
        return None

    def findIndexOfFirstFrogByName(self, name):
        for i, frog in enumerate(self.frogs):
            if frog.get('name') == name:
                return i
        return -1

    def getFrogByIndex(self, index):
        if 0 <= index < len(self.frogs):
            return self.frogs[index]
        return None

    def getFrogByName(self, name):
        for frog in self.frogs:
            if frog.get('name') == name:
                return frog
        return None

if __name__ == "__main__":
    frogs = Frogs()
