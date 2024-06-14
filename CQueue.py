class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


class CQueue:  # FIFO
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.pre = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def __repr__(self):
        if self.length:
            _str = ""
            temp = self.head
            while temp.next:
                _str += str(temp.data) + "<->"
                temp = temp.next
            else:
                _str += str(temp.data)
            return _str
        else:
            return "0"

    def __len__(self):
        return self.length

    def dequeue(self):
        if self.length <= 1:
            if self.length == 0:
                print("queue is empty")
            else:
                data = self.head.data
                self.head = None
                self.tail = None
                self.length -= 1
                return data
        else:
            data = self.tail.data
            self.tail = self.tail.pre
            self.tail.next = None
            self.length -= 1
            return data


cq = CQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)

print(cq.dequeue())
print(cq)


# deque way (best way)
from collections import deque
import logging

logging.basicConfig(format=" %(levelname)s: %(msg)s")

class DQueue:
    def __init__(self):
        self.container = deque()
    
    def enqueue(self,value):
        return self.container.appendleft(value)
    
    def dequeue(self):
        try:
            return self.container.pop()
        except:
            logging.warning('Queue is Empty')
        
    def is_empty(self):
        if len(self.container):
            return False
        else:
            return True
        
    def len(self):
        return len(self.container)
    
    def peek(self):
        return self.container[-1]
    
    def __repr__(self):
        return f'{self.container}'
    
my_queue = DQueue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.dequeue()
my_queue.dequeue()

print(my_queue)