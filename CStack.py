class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list way
class CStack:  # LIFO
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def pop(self):
        value = None
        if self.head:
            value = self.head.data
            self.head = self.head.next
        return value

    def isempty(self):
        if self.head:
            return False
        else:
            return True

    def __repr__(self):
        _str = ""
        if self.head:
            temp = self.head
            while temp.next:
                _str += str(temp.data) + "=>"
                temp = temp.next
            else:
                _str += str(temp.data)
            return _str
        else:
            return "0"


cs = CStack()
cs.push(1)
cs.push(2)
cs.push(3)
cs.push(4)
print(cs)

cs.pop()
print(cs)


# deque way (best way)
from collections import deque
import logging

logging.basicConfig(format=" %(levelname)s: %(msg)s")


class DStack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        try:
            return self.container.pop()
        except:
            logging.warning("empty queue")

    def peek(self):
        return self.container[-1]

    def isempty(self):
        if len(self.container):
            return True
        else:
            return False

    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return f"{self.container}"


my_stack = DStack()
my_stack.push(2)
my_stack.push(0)
my_stack.push(9)
print(my_stack)
print(my_stack.pop())
print(my_stack)
