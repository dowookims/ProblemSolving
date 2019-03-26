h1 = [6, 9, 5, 7, 4]
h2 = [3, 9, 9, 3, 5, 7, 2]
h3 = [1, 5, 3, 6, 7, 6, 5]
res = [0] * len(h2)
for i in range(len(h2)-1, 0,-1):
    flag = True
    for j in range(i-1, -1, -1):
        if h2[i] < h2[j]:
            res[i] = j+1
            flag = False
            break
    if flag:
        res[i] = 0

print(res)


