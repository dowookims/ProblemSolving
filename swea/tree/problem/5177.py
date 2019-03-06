import sys
sys.stdin = open("5177.txt", "r")


for TC in range(1, int(input())+1):
    n = int(input())
    case = list(map(int, input().split()))
    case.insert(0, 0)
    for i in range(1, n+1):
        if i > 1:
            if case[i//2] > case[i]:
                j = i
                while j > 1:
                    if case[j//2] > case[j]:
                        case[j], case[j//2] = case[j//2], case[j]
                    j = j//2
    res = 0
    idx = (len(case)-1)//2
    while idx > 0:
        res += case[idx]
        idx = idx // 2
    print("#{} {}".format(TC, res))



