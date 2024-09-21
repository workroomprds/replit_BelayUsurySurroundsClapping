#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Frogs:
    def __init__(self):
        self.frogs = []

    def newFrog(self):
        frog = {}  # You can expand this to include frog properties if needed
        self.frogs.append(frog)
        return frog

    def getFrogs(self):
        return self.frogs
