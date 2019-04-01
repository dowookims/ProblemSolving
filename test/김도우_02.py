def cal(n, m):
    global res


for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    case = [0] * N
    res = 0
    for i in range(N):
        case[i] = list(map(int, input().split()))
    d = [0]*6
    for i in range(1, N):
        for j in range(1, M-2):
            for k in range(j+1, M-1):



    print('{} {}'.format(TC, res))