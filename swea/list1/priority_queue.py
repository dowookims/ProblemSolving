class Node:
    def __init__(self,data, n=None):
        self.data = data
        self.next = None

def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None:
        front = newNode
    else:
        f = front
        pre = None
        while f:
            if f.item < newNode.item:
                pre = f
                f = f.next
            else:
                break
        if pre == None:
            front = newNode
            newNode.next = f
        elif f == None:
            pre.next = newNode
            rear = newNode
        else:
            pre.next = newNode
            newNode.next = f