#!/usr/bin/python2

class Index:
    def __init__(self, value=0):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value % 256

    def add_value(self, value):
        self.set_value(self.get_value() + value)

    def __str__(self):
        return chr(self.get_value())

    def __int__(self):
        return self.get_value()

    def __add__(self, other):
        return Index(int(self) + int(other))

