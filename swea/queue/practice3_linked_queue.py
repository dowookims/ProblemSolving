# import ctypes
# a = "hello world"
# print(ctypes.cast(id(a), ctypes.py_object).value)

class Node:
    def __init__(self,item, n=None):
        self.item = item
        self.next = n

class LinkedQueue:
    def __init__(self,n):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    def enQueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.front = newNode
        else :
            self.rear.next = newNode
        self.rear = newNode
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
            return None
        item = self.front.item
        self.front = self.front.next
        if self.isEmpty():
            self.rear = None
        return item

a = LinkedQueue(10)
a.enQueue(5)
a.enQueue(4)
a.enQueue(3)
print(a.deQueue())
print(a.deQueue())
print(a.deQueue())
