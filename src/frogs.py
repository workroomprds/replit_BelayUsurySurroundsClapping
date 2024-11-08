#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frogs:
    def __init__(self):
        self.frogs = []

    def newFrog(self, frog):
        self.frogs.append(frog)

    def getFrogs(self):
        return self.frogs

    def findFirstFrogByName(self, name):
        for index, frog in enumerate(self.frogs):
            if frog['name'] == name:
                return index
        return -1

    def findIndexOfFirstFrogByName(self, name):
        return self.findFirstFrogByName(name)

    def getFrogByIndex(self, index):
        if 0 <= index < len(self.frogs):
            return self.frogs[index]
        return None

    def getFrogByName(self, name):
        index = self.findFirstFrogByName(name)
        if index != -1:
            return self.frogs[index]
        return None

    def countFrogs(self):
        return len(self.frogs)

    def binThisFrog(self, name):
        index = self.findFirstFrogByName(name)
        if index != -1:
            del self.frogs[index]
            return True
        return False
