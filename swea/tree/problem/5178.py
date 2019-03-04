import sys
sys.stdin = open("5178.txt", "r")

def postOrder(T):
    if T == 0:
        return

    if tree[T]:
        i = T//2
        tree[i] = tree[T] + tree[T+1]
        postOrder(i)

for TC in range(1,int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        idx, v = map(int, input().split())
        tree[idx] = v
    k = 0
    while N > 2**k-1:
        k += 1

    if 2**k > N:
        k -= 1

    postOrder(2**k)
    for i in range(len(tree)):
        if not tree[i]:
            print(i, end=" ")
    print()
    print("#{} {}".format(TC, tree[L]))
