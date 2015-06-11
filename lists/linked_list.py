class Underflow(Exception):
    pass


class Overflow(Exception):
    pass


class Node:
    data = None
    link = None


class AvailableSpace:
    """ Storage pool based on with linked list"""
    available = Node(link=Node(link=Node(link=Node(link=Node()))))

    def get_node(self):
        if self.available is None:
            raise Overflow()
        else:
            result = self.available
            self.available = self.available.link
            return result

    def release(self, node):
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
