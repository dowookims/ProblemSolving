import sys
sys.stdin = open("1979.txt", "r")

for TC in range(1, int(input())+1):
    n, k = map(int, input().split())
    case = [0]*n
    res = 0

    for i in range(n):
        case[i] = list(map(int, input().split()))
        if len(case[i]) >= k:
            j = 0
            while True:
                if j >= n:
                    break

                elif case[i][j]:
                    cnt = 1
                    while True:
                        j += 1
                        if j == n and cnt == k:
                            res += 1
                        elif j >= n:
                            break
                        elif case[i][j]:
                            cnt += 1
                        elif not case[i][j] and cnt != k:
                            break
                        elif not case[i][j] and cnt == k:
                            res += 1
                            break
                else:
                    j += 1
    for c in range(n):
        r = 0
        while True:
            if r >= n:
                break
            elif case[r][c]:
                cnt = 1
                while True:
                    r += 1
                    if r == n and cnt == k:
                        res += 1
                    elif r >= n:
                        break
                    elif case[r][c]:
                        cnt += 1
                    elif not case[r][c] and cnt != k:
                        break
                    elif not case[r][c] and cnt == k:
                        res += 1
                        break
            else:
                r += 1
    print("#{} {}".format(TC, res))
