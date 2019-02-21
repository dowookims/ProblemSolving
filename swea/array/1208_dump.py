import sys
sys.stdin = open("input3.txt", "r")

for TC in range(1,11):
    dump = int(input())
    case = list(map(int, input().split()))
    res = 0
    for i in range(dump+1):
        min_dump = case[0]
        min_x = 0
        max_dump = case[0]
        max_x = 0
        for j in range(1,100):
            if case[j]<min_dump:
                min_dump = case[j]
                min_x = j
            elif case[j]> max_dump:
                max_dump = case[j]
                max_x = j
            if i==dump:
                res = max_dump-min_dump
        case[min_x] += 1
        case[max_x] -= 1

    print(f"#{TC} {res}")