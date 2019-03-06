import sys
sys.stdin = open("1233.txt","r")


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(nd):
    global res
    if nd:
        preorder(nd.left)
        preorder(nd.right)
        if not isinstance(nd.data, int):
            if len(s)<2:
                res = 1
                return
            b = s.pop()
            a = s.pop()
            if not isinstance(a,int) or not isinstance(b, int):
                res = 0
                return

            if nd.data == "*":
                s.append(a * b)
            elif nd.data == "/":
                if b == 0:
                    b = 1
                s.append(a / b)
            elif nd.data == "+":
                s.append(a + b)
            else:
                s.append(a - b)
        else:
            s.append(nd.data)


for TC in range(1, 11):
    n = int(input())
    case = [Node(None) for _ in range(n+1)]
    s = []
    res = 1
    for _ in range(n):
        i = input().split()
        if len(i) == 4:
            node = case[int(i[0])]
            node.data = i[1]
            node.left = case[int(i[2])]
            node.right = case[int(i[3])]
        else:
            if i[1].isdigit():
                case[int(i[0])].data = int(i[1])
            else:
                res = 0
    if res:
        preorder(case[1])
    print("#{} {}".format(TC, res))

