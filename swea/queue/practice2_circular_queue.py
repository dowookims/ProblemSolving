class Queue():
    def __init__(self,n):
        self.queue = [0]*n
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return (self.rear+1) % len(self.queue) == self.front
    
    def enQueue(self, item):
        if self.isFull():
            print("Queue Full")
        else:
            self.rear = (self.rear+1) % len(self.queue)
            self.queue[self.rear] = item
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]

a = Queue(10)
for i in range(1,20):
    a.enQueue(i)
for i in range(8):
    print(a.deQueue())