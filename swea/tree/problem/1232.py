import sys
sys.stdin = open("1232.txt", "r")


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left =left
        self.right = right


def preorder(nd):
    if nd:
        preorder(nd.left)
        preorder(nd.right)
        if not isinstance(nd.data, int):
            b = s.pop()
            a = s.pop()
            if nd.data == "*":
                s.append(a * b)
            elif nd.data == "/":
                s.append(a / b)
            elif nd.data == "+":
                s.append(a + b)
            else:
                s.append(a - b)
        else:
            s.append(nd.data)


for TC in range(1, 11):
    n = int(input())
    nl = [Node(None) for _ in range(n+1)]
    s = []
    for _ in range(n):
        i = input().split()
        if len(i) == 4:
            node = nl[int(i[0])]
            node.data = i[1]
            node.left = nl[int(i[2])]
            node.right = nl[int(i[3])]
        else:
            nl[int(i[0])].data = int(i[1])

    preorder(nl[1])
    print("#{} {}".format(TC, int(s.pop())))