import sys
sys.stdin = open("number_array.txt", "r")

for TC in range(1, int(input())+1):
    r = int(input())
    case = [[] for _ in range(r)]
    for i in range(r):
        case[i] = list(map(int, input().split()))

    print(f"#{TC}")
    for i in range(r):
        for j in range(r-1,-1,-1):
            print(case[j][i], end="")
        print(end=" ")
        for k in range(r-1,-1,-1):
            print(case[r-i-1][k], end="")
        print(end=" ")
        for l in range(r):
            print(case[l][r-i-1], end="")
        print()

