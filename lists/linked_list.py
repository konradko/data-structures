class Underflow(Exception):
    pass


class Overflow(Exception):
    pass


class Node:

    def __init__(self, link=None, data=None):
        self.link = link
        self.data = data


class AvailableSpace:
    """ Storage pool based on a linked list"""

    def __init__(self, size):
        self.available = None

        for x in xrange(size):
            self.available = Node(link=self.available)

    def get_node(self):
        if self.available is None:
            raise Overflow()
        else:
            result = self.available
            self.available = self.available.link
            return result

    def release(self, node):
        node.data = None
        node.link = self.available
        self.available = node


class Stack(AvailableSpace):
    pointer = None

    def stack(self, item):
        node = self.get_node()
        node.data = item
        node.link = self.pointer
        self.pointer = node

    def unstack(self):
        if self.pointer is None:
            raise Underflow()
        else:
            node = self.pointer
            self.pointer = node.link
            result = node.data
            self.release(node)
            return result


class Queue(AvailableSpace):
    front = None
    rear = None

    def queue(self, item):
        node = self.get_node()
        node.data = item
        node.link = None
        if self.front is None:
            self.front = node
        else:
            self.rear.link = node
            self.rear = node

    def unqueue(self):
        if self.front is None:
            raise Underflow()
        else:
            node = self.front
            self.front = node.link
            result = node.data
            self.release(node)
            return result


class Deque(Queue):

    def front_insert(self, item):
        node = self.get_node()
        node.data = item
        node.link = self.front
        if self.front is None:
            self.rear = node
        self.front = node

    def rear_delete(self):
        if self.front is None:
            raise Underflow()

        if self.front == self.rear:
            self.front = None
            result = self.rear.data
            self.release(self.rear)
        else:
            node = self.front
            while node.link != self.rear:
                node = node.link
            node.link = None
            result = self.rear.data
            self.release(self.rear)
            self.rear = node

        return result


class CircularList(AvailableSpace):
    pointer = None

    def left_insert(self, item):
        node = self.get_node()
        node.data = item
        if self.pointer is None:
            self.pointer = node
        else:
            node.link = self.pointer.link
        self.pointer.link = node

    def right_insert(self, item):
        self.left_insert(item)
        self.pointer = self.pointer.link

    def left_delete(self):
        if self.pointer is None:
            raise Underflow()

        node = self.pointer.link
        if self.pointer == node:
            self.pointer = None
        else:
            self.pointer.link = node.link

        result = node.data
        self.release(node)
        return result

    def right_delete(self):
        if self.pointer is None:
            raise Underflow()

        node = self.pointer.link
        if self.pointer == node:
            self.pointer = None
            result = node.data
            self.release(node)
        else:
            while node.link != self.pointer:
                node = node.link
            node.link = None
            result = self.pointer.data
            self.release(self.pointer)
            self.pointer = node

        return result

    def erase(self):
        if self.pointer is not None:
            node = self.available
            self.available = self.pointer.link
            self.pointer.link = node
            self.pointer = None

    def concatenate(self, other_circular_list):
        if other_circular_list.pointer is not None:
            if self.pointer is not None:
                node = self.pointer.link
                self.pointer.link = other_circular_list.pointer.link
                other_circular_list.pointer.link = node
            self.pointer = other_circular_list.pointer
            other_circular_list.pointer = None
