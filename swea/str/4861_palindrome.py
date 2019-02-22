import sys
sys.stdin = open("sample_input2.txt", "r")

for TC in range(1, int(input())+1):
    N,M = list(map(int, input().split()))
    case = [[] for _ in range(N)]
    res = ''
    for i in range(N):
        case[i] = input()
    for r in range(N):
        for i in range(N-M+1):
            sen = case[r][i:i+M]
            if sen == sen[::-1]:
                res = sen
                break
            sen2 =''
            for j in range(i, i+M):
                sen2 += case[j][r]
            if sen2 == sen2[::-1]:
                res = sen2
                break
        if res:
            break
    print(f"#{TC} {res}")