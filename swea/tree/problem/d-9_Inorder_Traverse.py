import sys
sys.stdin = open("d9.txt", "r")


def inorder_traverse(T):
        if tree[T][0]:
            inorder_traverse(tree[T][0]-1)
        print(word[T], end="")
        if tree[T][1]:
            inorder_traverse(tree[T][1]-1)


for TC in range(1, 11):
    v = int(input())

    tree = [[0 for _ in range(2)] for _ in range(v)]

    word = ['' for _ in range(v)]
    for i in range(v):
        items = input().split()
        word[i] = items[1]
        if len(items)>= 3:
            tree[i][0] = int(items[2])
            if len(items)==4:
                tree[i][1] = int(items[3])
    print("#{} ".format(TC),end=" ")
    inorder_traverse(0)
    print()



