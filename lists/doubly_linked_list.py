class Underflow(Exception):
    pass


class Overflow(Exception):
    pass


class Node:

    def __init__(self, right_link=None, left_link=None, data=None):
        self.right_link = right_link
        self.left_link = left_link
        self.data = data


class AvailableSpace:
    """ Storage pool based on a linked list with doubly linked list nodes"""

    def __init__(self, size):
        self.available = None

        for x in xrange(size):
            self.available = Node(right_link=self.available)

    def get_node(self):
        if self.available is None:
            raise Overflow()
        else:
            result = self.available
            self.available = self.available.right_link
            return result

    def release(self, node):
        node.data = None
        node.left_link = None
        node.right_link = self.available
        self.available = node


class DoublyLinkedList(AvailableSpace):
    left_end = None
    right_end = None

    def left_insert(self, item):
        node = self.get_node()
        node.data = item
        node.left_link = None
        node.right_link = self.left_end
        if self.left_end is None:
            self.right_end = node
        else:
            self.left_end.link = node
        self.left_end = node

    def right_insert(self, item):
        node = self.get_node()
        node.data = item
        node.right_link = None
        node.left_link = self.right_end
        if self.right_end is None:
            self.left_end = node
        else:
            self.right_end.link = node
        self.right_end = node

    def left_delete(self):
        if self.left_end is None:
            raise Underflow()
        node = self.left_end
        self.left_end = node.right_link
        if self.left_end is None:
            self.right_end = None
        else:
            self.left_end.left_link = None
        result = node.data
        self.release(node)
        return result

    def right_delete(self):
        if self.right_end is None:
            raise Underflow()
        node = self.right_end
        self.right_end = node.left_link
        if self.right_end is None:
            self.left_end = None
        else:
            self.right_end.right_link = None
        result = node.data
        self.release(node)
        return result
