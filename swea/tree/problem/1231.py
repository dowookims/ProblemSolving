import sys
sys.stdin = open("1231.txt", "r")

def inorder_traverse(T):
    global n
    if T*2 < n+1:
        inorder_traverse(T*2)
    print(tree[T], end="")
    if T*2+1 < n+1:
        inorder_traverse(T*2+1)


for TC in range(1,11):
    n = int(input())
    tree = [0]*(n+1)
    for i in range(1, n+1):
        item = input().split()
        tree[int(item[0])] = item[1]
    print("#{}".format(TC), end=" ")
    inorder_traverse(1)
    print()