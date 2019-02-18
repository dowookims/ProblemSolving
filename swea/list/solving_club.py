TC = int(input())
for case_num in range(1, TC+1):
    nasa_cnt = int(input())
    nasa_inf = list(map(int, input().split()))

    # 나사 분해
    nasa_tuple = []
    for i in range(0, len(nasa_inf), 2):
        nasa_tuple.append([nasa_inf[i], nasa_inf[i+1]])

    #나사 연결 길이 비교

    for i in range(len(nasa_tuple)-1):
        min = i
        for j in range(i+1, len(nasa_tuple)):
            if nasa_tuple[min][1] > nasa_tuple[j][1]:
                min = j
        nasa_tuple[i], nasa_tuple[min] = nasa_tuple[min], nasa_tuple[i]


    for i in range(len(nasa_tuple)-1):
        if not nasa_tuple[i][1] == nasa_tuple[i+1][0]:
            for j in range(i+2, len(nasa_tuple)):
                if nasa_tuple[i][1] == nasa_tuple[j][0]:
                    nasa_tuple[j], nasa_tuple[i+1] = nasa_tuple[i+1], nasa_tuple[j]

    c = ""
    for item in nasa_tuple:
        c +=' '.join(list(map(str, item)))+' '
    print(f"#{case_num} {c}")

'''
for t in range(int(input())):
    n = int(input())
    list_1 = [x for x in input().split()]
    list_2 = []
    for i in range(n):
        t1 = list_1.pop(0)
        t2 = list_1.pop(0)
        list_2.append((t1,t2))
    for i in range(n-1,0,-1):
        ischanged = False
        for j in range(i):
            if list_2[i][0] == list_2[j][-1]:
                temp = list_2.pop()
                list_2[j]+=temp
                ischanged = True
                break
        if not ischanged:
            for j in range(i):
                if list_2[i][-1] == list_2[j][0]:
                    temp = list_2.pop()
                    list_2[j] = temp+list_2[j]
                    break
    list_2 = list(list_2[0])
    print(f"#{t+1} {' '.join(list_2)}")
'''





