import sys
sys.stdin = open("solv1.txt", "r", encoding="utf8")

for TC in range(1, 11):
    r = int(input())
    case = [[] for _ in range(8)]
    cnt = 0
    for i in range(8):
        case[i] = input()
    for i in range(8):
        for j in range(0, 8-r+1):
            right = ''
            bottom = ''
            for k in range(r):
                right += case[i][j+k]
                bottom += case[j+k][i]
            if right == right[::-1]:
                cnt +=1
            if bottom == bottom[::-1]:
                cnt +=1


    print(f"#{TC} {cnt}")
