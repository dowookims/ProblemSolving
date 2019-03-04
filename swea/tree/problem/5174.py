
'''
[파이썬 S/W 문제해결 기본] 8일차 - subtree
'''
import sys
sys.stdin = open("5174.txt", "r", encoding="utf-8")

def preorder_traverse(T):
    global res
    for item in tree[T]:
        if item:
            res += 1
            preorder_traverse(item)


for TC in range(1, int(input())+1):
    E, N = map(int, input().split())
    case = list(map(int, input().split()))
    tree = [[0 for _ in range(2)] for _ in range(E+2)]
    res = 1
    for i in range(0, len(case), 2):
        if not tree[case[i]][0]:
            tree[case[i]][0] = case[i+1]
        else:
            tree[case[i]][1] = case[i+1]
    preorder_traverse(N)
    print("#{} {}".format(TC, res))