import sys
sys.stdin = open("5120.txt","r")

for TC in range(1,int(input())+1):
    N,M,K = map(int,input().split())
    case = list(map(int, input().split()))
    m = 0
    for i in range(1, K+1):
        m += M
        if m>len(case):
            m = m-len(case)
        case.insert(m, 0)
        f = m+1
        if m == len(case)-1:
            f = 0
        case[m] = case[m-1] + case[f]
    print(f"#{TC}", end=" ")
    for i in range(len(case)-1, len(case)-11,-1):
        if i== -1:
            break
        print(case[i], end=" ")
    print()