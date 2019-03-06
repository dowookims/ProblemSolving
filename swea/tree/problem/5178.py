import sys
sys.stdin = open("5178.txt", "r")

def post_traverse(T):
    global N
    if T*2 > N:
        return
    else:
        post_traverse(T*2)
        if T*2+1 <= N:
            post_traverse(T*2+1)
            tree[T] = tree[T*2] + tree[T*2+1]
        else:
            tree[T] = tree[T*2]


for TC in range(1,int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        idx, v = map(int, input().split())
        tree[idx] = v
    post_traverse(1)
    print("#{} {}".format(TC, tree[L]))
