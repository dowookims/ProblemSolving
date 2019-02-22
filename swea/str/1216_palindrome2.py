import sys
sys.stdin = open("input1.txt", "r")

def findPal(case, r):
    # 열 기준 검색
    for i in range(100):
        for j in range(0, 100-r+1):
            s = j
            e = j+r-1
            #행 기준 체크
            for k in range(0, r//2):
                if case[i][s+k] != case[i][e-k]:
                    break
                if k == r//2-1:
                    return True
            # 열 기준 체크
            for k in range(0, r//2):
                if case[s+k][i] != case[e-k][i]:
                    break
                if k == r//2-1:
                    return True
    return False


for _ in range(10):
    TC = int(input())
    case = [ [] for _ in range(100) ]
    res = 0
    for i in range(100):
        case[i] = input()
    # 길이 정하기
    for i in range(100,0,-1):
        isFound = findPal(case, i)
        if isFound:
            res = i
            break

    print(f'#{TC} {res}')