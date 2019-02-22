import sys
sys.stdin = open("input9.txt", "r")
for _ in range(10):
    TC = int(input())
    n, s = list(map(int, input().split()))
    print(f"#{TC} {n**s}")