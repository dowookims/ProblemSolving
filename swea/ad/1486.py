'''
1486 : 장훈이의 높은 선반
'''
import sys
sys.stdin = open("1486.txt", "r")


def sol(s=0, idx = 0):
    global B
    global N
    global res
    if res == 0:
        return
    if s >= B:
        if s-B == 0:
            res = 0

        elif res > s-B:
            res = s-B
        return
    for i in range(idx, N):
        if not visited[i]:
            s += people[i]
            visited[i] = 1
            sol(s, i)
            s -= people[i]
            visited[i] = 0


for TC in range(1, int(input())+1):
    N, B = map(int, input().split())
    visited = [0] * N
    people = list(map(int, input().split()))
    res = 987654321
    sol()
    print("#{} {}".format(TC, res))

'''
def rec(i, h):
    global ans
    if i < N and ans != B:
        temp = h+H[i]
        if temp < ans:
            rec(i+1, temp)
            if temp >= B:
                ans = temp
        rec(i+1, h)
 
for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = float('inf')
    rec(0, 0)
    print('#{} {}'.format(tc, ans-B))
'''