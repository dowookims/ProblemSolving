import sys
sys.stdin = open('1865.txt', "r")


def cal(s=1, d=0):
    global N
    global res
    if d == N:
        if s > res:
            res = s
    else:
        for i in range(N):
            if case[d][i] == 0:
                continue
            elif not visited[i]:
                visited[i] = 1
                if s * case[d][i] > res:
                    cal(s * case[d][i], d+1)
                visited[i] = 0



for TC in range(1, int(input())+1):
    N = int(input())
    visited = [0]*N
    case = [0]*N
    m = 0
    res = 0
    for i in range(N):
        case[i] = list(map(lambda x: int(x)/100, input().split()))
    cal()
    print('#{0} {1:.6f}'.format(TC, res*100))

'''
순열의 BigO = O(n!)
이렇게 될 경우 실행속도가 극악이 되기 때문에
가지치기를 해줌으로 계산수를 제거해 줘야 함
이를 생각하는게 확률의 곱이 점점 작아지는 것을 활용하여 이용
'''