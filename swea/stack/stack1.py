TC = int(input())+1
for i in range(1, TC):
    a = int(input())//10
    d = [0]*(a+1)
    d[0] = 0
    d[1] = 1
    d[2] = 3
    d[3] = 5
    if a>= 4:
        for j in range(4, a+1):
            d[j] =  d[j-1]+d[j-2]*2
    print(f'#{i} {d[a]}')