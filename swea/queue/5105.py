import sys
sys.stdin = open("5105.txt", "r")

class Queue:
    def __init__(self,size,init=None):
        self.size=size
        self.init=init
        self.storage=[self.init]*self.size
        self.front=-1
        self.rear=-1

    def enQueue(self,item):
        self.rear+=1
        self.storage[self.rear]=item

    def deQueue(self):
        self.front+=1
        return self.storage[self.front]

    def isEmpty(self):
        return self.front==self.rear

def isWall(r, c):
    global n
    return 0 <= r <n and 0 <= c <n

def next(r, c, sum):
    result = []
    dr=[0, 0, 1, -1]
    dc=[1, -1, 0, 0]
    for i in range(4):
        tr = r+dr[i]
        tc = c+dc[i]
        if isWall(tr,tc):
            if board[tr][tc]=='3':
                return 1
            elif board[tr][tc]=='0':
                result.append((tr,tc,sum+1))
                board[tr][tc]='1'
    return result

def sol(r,c,sum):
    temp = next(r, c, sum)
    if temp == True:
        return sum
    else:
        for i in temp:
            q.enQueue(i)
    return 0

for tc in range(1,int(input())+1):
    n=int(input())
    board=[list(input()) for _ in range(n)]
    q=Queue(n**2)
    check=False
    for i in range(n):
        for j in range(n):
            if board[i][j]=='2':
                q.enQueue((i,j,0))
                check=True
                break
        if check:
            break
    check=False
    result=0
    while(not q.isEmpty()):
        temp=sol(*(q.deQueue()))
        if temp!=0:
            result=temp
            break
    print("#{} {}".format(tc, result))