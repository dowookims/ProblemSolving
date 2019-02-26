import sys
sys.stdin = open("5097.txt", "r")

class Queue:
    def __init__(self, n):
        self.queue = []
        self.front = -1
        self.rear = -1

    def enQueue(self, item):
        if self.rear == -1:
            self.rear + 1
            self.queue.append(item)
    def deQueue(self):
        self.front += 1
        return self.queue[self.front]



for TC in range(1,int(input())+1):
    N, M = list(map(int ,input().split()))
    case = list(map(int,input().split()))
    a = Queue(M)
    for i in range(M+1):
        a.enQueue(case[i%N])
        if i == M:
            break
        a.deQueue()
    print(f"#{TC} {a.deQueue()}")