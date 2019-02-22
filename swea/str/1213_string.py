import sys
sys.stdin = open("test_input1.txt", "r", encoding="UTF8")

for _ in range(10):
    TC = int(input())
    conditions = input()
    cases = input()
    res = 0
    for i in range(len(cases)-len(conditions)+1):
        if cases[i] == conditions[0]:
            cnt = 1
            for j in range(1,len(conditions)):
                if conditions[j] == cases[i+j]:
                    cnt +=1
            if cnt == len(conditions):
                res +=1
    print(f"#{TC} {res}")

