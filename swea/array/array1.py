import sys
sys.stdin = open("input1.txt", "r")

for TC in range(1, int(input())+1):
    a = int(input())
    score = [0]*101
    case = list(map(int, input().split()))
    for i in range(len(case)):
        score[case[i]] +=1
    res = 0

    for i in range(1, len(score)):
        if score[i] >= score[res]:
            res = i
    print(f"#{TC} {res}")


