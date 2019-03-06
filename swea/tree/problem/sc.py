import sys
sys.stdin = open("sc.txt", "r")
'''
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
 
def preorder(nd):
    if nd:
        preorder(nd.left)
        preorder(nd.right)
        if not isinstance(nd.data, int):
            b=s.pop()
            a=s.pop()
            if nd.data=="*":
                s.append(a*b)
            elif nd.data=="/":
                s.append(a/b)
            elif nd.data=="+":
                s.append(a+b)
            else:
                s.append(a-b)
        else:
            s.append(nd.data)
 
for tc in range(1,11):
    n=int(input())
    ns=[Node(None) for _ in range(n+1)]
    s=[]
    for _ in range(n):
        i=input().split()
        if len(i)==2:
            ns[int(i[0])].data=int(i[1])
        else:
            nd=ns[int(i[0])]
            nd.data=i[1]
            nd.left=ns[int(i[2])]
            nd.right=ns[int(i[3])]
    preorder(ns[1])
    print(f"#{tc} {int(s.pop())}")
'''

def post_traverse(T):
    global n
    if T<n:
        post_traverse(T * 2)
        post_traverse(T*2+1)

    if case[T][0] == '+':
        case[T][0] = case[case[T][1]]+ case[case[T][2]]
    elif case[T][0] == '-':
        case[T][0] = case[case[T][1]] - case[case[T][2]]
    elif case[T][0] == '*':
        case[T][0] = case[case[T][1]] * case[case[T][2]]
    elif case[T][0] == '/':
        case[T][0] = case[case[T][1]] / case[case[T][2]]

for TC in range(1, 11):
    n = int(input())
    case = [0]*(n+1)
    for i in range(n):
        items = input().split()
        if len(items) == 2:
            case[int(items[0])] = [int(items[1]), -1]
        else:
            case[int(items[0])] = [items[1], int(items[2]), int(items[3])]
    post_traverse(1)
    print("#{} {}".format(TC, int(case[1])))