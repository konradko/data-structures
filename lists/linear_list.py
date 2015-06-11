class Underflow(Exception):
    pass


class Overflow(Exception):
    pass


class SequentialMemory:
    """ Sequential area of memory based on linear list """
    memory = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    max_nodes = len(memory)

    def set_node(self, address, node):
        self._list[address - 1] = node

    def remove_node(self, address):
        value = self._list[address - 1]
        self._list[address - 1] = str(address - 1)
        return value


class Stack(SequentialMemory):
    stack_pointer = 0

    def stack(self, node):
        """ Insert a new node """
        if self.stack_pointer == self.max_nodes:
            raise Overflow()
        self.stack_pointer += 1
        self.set_node(self.stack_pointer, node)

    def unstack(self):
        """ Return the top item and delete it from the stack"""
        if self.stack_pointer == 0:
            raise Underflow()
        else:
            self.stack_pointer -= 1
            return self.remove_node(self.stack_pointer)


class Queue(SequentialMemory):
    rear_node_address = 0
    last_removed_node_address = 0
    number_of_nodes = 0

    def queue(self, node):
        """ Insert a new node """
        if self.number_of_nodes == self.max_nodes:
            raise Overflow()

        self.number_of_nodes += 1
        if (self.rear_node_address == self.max_nodes):
            self.rear_node_address = 1
        else:
            self.rear_node_address = self.rear_node_address + 1
        self.set_node(self.rear_node_address, node)

    def unqueue(self):
        """ Return the front item and delete it from the queue """
        if self.number_of_nodes == 0:
            raise Underflow()

        self.number_of_nodes -= 1
        if (self.last_removed_node_address == self.max_nodes):
            self.last_removed_node_address = 1
        else:
            self.last_removed_node_address = self.last_removed_node_address + 1

        return self.remove_node(self.last_removed_node_address)


class Deque(Queue):

    def front_insert(self, node):
        """ Insert a new node in the front of deque """
        if self.number_of_nodes == self.max_nodes:
            raise Overflow()

        self.number_of_nodes += 1
        self.set_node(self.last_removed_node_address, node)
        if self.last_removed_node_address == 1:
            self.last_removed_node_address = self.max_nodes
        else:
            self.last_removed_node_address = self.last_removed_node_address - 1

    def rear_delete(self):
        """ Return the rear item and delete it from the deque """
        if self.number_of_nodes == 0:
            raise Underflow()

        self.number_of_nodes -= 1
        result = self.remove_node(self.rear_node_address)
        if self.rear_node_address == 1:
            self.rear_node_address = self.max_nodes
        else:
            self.rear_node_address = self.rear_node_address - 1
        return result
