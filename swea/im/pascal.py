for TC in range(1, int(input())+1):
    n = int(input())
    d = [[]for _ in range(n+1)]
    d[0] = [0]
    d[1] = [1]
    if n>1:
        d[2] = [1, 1]
    if n>2:
        for i in range(3, n+1):
            for j in range(0, i):
                if j == 0:
                    d[i].append(1)
                elif j == i-1:
                    d[i].append(1)
                else:
                    d[i].append(d[i-1][j-1]+d[i-1][j])
    print("#{}".format(TC))
    for i in range(1, n+1):
        for j in range(len(d[i])):
            print(d[i][j], end=" ")
        print()