class Queue():
    
    def __init__(self):
        self.q = [0]*10000
        self.front = -1
        self.rear = -1
    def enQueue(self, n):
        self.rear += 1
        self.q[self.rear] = n
    def deQueue(self):
        self.front += 1
        return print(self.q[self.front])

    def isEmpty(self):
        return self.front == self.rear


    def isFull(self):
        return self.rear == len(self.q)-1
    
    def qPeek(self):
        if self.isEmpty() : print("Queue_EMpty")
        else : return self.q[self.front+1]

a = Queue()

a.enQueue(1)
a.enQueue(2)
a.enQueue(3)

a.deQueue()
a.deQueue()
a.deQueue()