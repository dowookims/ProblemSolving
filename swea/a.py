T = 10
for _ in range(T):
    TC = int(input())
    ladder = [[]] * 100
    for i in range(100):
        ladder[i] = list(map(int,input().split()))

    point = 0
    col = 98
    d = 1
    for i in range(100):
        if ladder[99][i] == 2:
            point = i

    while True:
        if ladder[col][point]:
            point -= 1
        elif ladder[col-1][point]:
            col -= 1
        if col == 0:
            break
    print(f"#{TC} {point}")