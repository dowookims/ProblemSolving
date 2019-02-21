import sys
sys.stdin = open("input6.txt", "r")
for _ in range(10):
    TC = int(input())
    case = [[] for _ in range(100)]
    for i in range(100):
        case[i] = list(map(int, input().split()))
    res = 0
    start_list =''
    for i in range(100):
        if case[0][i]:
            start_list +=' '+str(i)
    start_list = list(map(int, start_list.split()))
    c = [1]*len(start_list)
    move_list = [0]*len(start_list)
    result = []
    while True:
        for i in range(len(start_list)):
            if start_list[i]>0 and case[c[i]][start_list[i]-1]:
                while True:
                    start_list[i] -=1
                    move_list[i] += 1
                    if start_list[i] == 0:
                        break
                c[i] +=1
            elif start_list[i]<99 and case[c[i]][start_list[i]+1]:
                while True:
                    start_list[i] +=1
                    move_list[i] += 1
                    if start_list[i] == 99:
                        break
                c[i] += 1
            move_list[i] += 1
            if c[i] == 99 and case[c[i]][start_list[i]] == 2:
                result.append(start_list[i])
            if c[0] == 99 and i==len(start_list)-1:
                break
        break
    res = result[0]
    for i in range(len(result)):
        if result[i]<res:
            res = result[i]
    print(f"#{TC} {res}")