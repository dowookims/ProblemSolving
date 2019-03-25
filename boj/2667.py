def isWall(r,c):
    global n
    return 0<= r <n and 0<= c <n

def is_home(r,c):
    global N
    if int(case[r][c]) == 1:
        case[r][c] == N
        d[N] += 1
        for i in range(4):
            mr = r + dr[i]
            mc = c + dc[i]
            if isWall(mr, mc) and case[mr][mc] == 1:
                is_home(mr, mc)


dr = [-1,0,1,0]
dc = [0,1,0,-1]
d = [0]*25
n = int(input())
case = [0]*n
for i in range(n):
    case[i] = input()

N = 1
for i in range(n):
    for j in range(n):
        if int(case[i][j]) == 1:
            N += 1
            is_home(i, j)
print(N)
for i in range(1, N+1):
    print(d[i])