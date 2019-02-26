# import ctypes
# a = "hello world"
# print(ctypes.cast(id(a), ctypes.py_object).value)

class Node:
    def __init__(self,item, n=None):
        self.item = item
        self.next = n

class LinkedQueue:
    def __init__(self,n):
        self.queue = [None]*n
        self.front = None
        self.rear = None
        self.cnt = -1
    
    def isEmpty(self):
        return self.front == None
    
    def enQueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.front = newNode
        else :
            self.rear.next = newNode
        self.rear = newNode
        self.cnt +=1
        self.queue[self.cnt] = newNode.item
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
            return None
        item = self.front.item
        self.front = self.front.next
        if self.isEmpty():
            self.rear = None

        self.queue[self.cnt] = None
        self.cnt -= 1
        return item

a = LinkedQueue(10)
a.enQueue(5)
a.enQueue(4)
a.enQueue(3)
print(a.cnt)
print(a.deQueue())
print(a.deQueue())
print(a.deQueue())
