import sys
sys.stdin = open("input6.txt", "r")
for _ in range(10):
    TC = int(input())
    res = 0
    case = [[] for _ in range(100)]
    start_list = []
    for i in range(100):
        case[i] = list(map(int, input().split()))
    for i in range(100):
        if case[0][i]:
            start_list.append(i)

    move_count = [0]*len(start_list)
    cnt = 0
    result = []
    for s in start_list:
        x_axios = s
        for y_axios in range(1,99):
            if x_axios>0 and case[y_axios][x_axios-1]:
                while x_axios>0 and case[y_axios][x_axios-1]:
                    x_axios -= 1
                    move_count[cnt] +=1
            elif x_axios<99 and case[y_axios][x_axios+1]:
                while x_axios<99 and case[y_axios][x_axios+1]:
                    x_axios += 1
                    move_count[cnt] +=1
            move_count[cnt] += 1
        cnt += 1
    min_value = move_count[0]
    min_index = 0
    for i in range(1, len(move_count)):
        if move_count[i] < min_value:
            min_value = move_count[i]
            min_index = i
    print(f"#{TC} {start_list[min_index]}")