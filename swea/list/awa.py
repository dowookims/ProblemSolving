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