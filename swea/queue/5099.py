import sys
sys.stdin = open("5099.txt", "r")

for TC in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    case = list(map(int, input().split()))
    fire = []
    c = N
    res = 0
    for i in range(N):
        fire.append([case[i],i+1])
    while len(fire)>1:
        p = fire.pop(0)
        if p[0] == 0 and c < M:
            fire.append([case[c], c+1])
            c += 1
        elif c<M:
            p[0] == p[0]//2
            fire.append([p[0], p[1]])
        elif c == M:
            if p[0] == 0:
                continue
            elif len(fire) == 0:
                res =p[1]
                break
            else:
                p[0] = p[0] // 2
                fire.append([p[0], p[1]])

    print(fire[0][1])
    print("#")




'''
1. 화덕에 피자 n개를 돌린다

2.화덕에 있는 피자가 다 녹을때까지 돌린다

3.다 돌린 피자가 있다면
  그 피자를 빼고 
  그 위치에 
  다음 피자를 넣는다

4. 이제 슬슬 피자가 빠져 나가서 피자가 하나 남을 때 
         그 피자의 번호를 반환한다.
'''