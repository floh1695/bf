#!/usr/bin/python2

class Node:
    def __init__(self):
        self.node_parent = None
        self.node_child = None
        self.node_last = None
        self.node_next = None

    def get_parent(self):
        return self.node_parent

    def get_child(self):
        return self.node_child

    def get_next(self):
        return self.node_next

    def get_last(self):
        return self.node_last

    def set_parent(self, node_parent):
        pass

# If I added this I don't think it will ever be useful
#    def set_child(self, node_child):
#        pass

    def set_next(self, node_next):
        self.node_next = node_next
        node_next.node_last = self

# This probably will never be used.
#    def set_last(self, node_last):
#        self.node_last = node_last
#        node_last.node_next = self

    def get_head(self):
        node_current = self
        while True:
            node_next = node_current.get_last()
            if node_next:
                node_current = node_next
            else:
                break
        return node_current

