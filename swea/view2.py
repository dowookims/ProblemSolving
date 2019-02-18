a = int(input())
for i in range(1, a+1):
    b = list(map(int,input().split()))
    w_c = 0
    for j in b:
        if j == 0:
            if b[j] > b[j+1] and b[j] > b[j+2]:
                w_c = b[j] - max(b[j+1], b[j+2])
        elif j == 1 or len(b)-2:
            if b[j] >b[j+1] and b[j+2] and b[j-1]:
                w_c = b[j]=max(b[j-1], b[j+1], b[j+2])
        elif j == len(b)-1:
            if b[j] > b[j-1] and b[j] > b[j-2]:
                w_c = b[j] - max(b[j-1], b[j-2])
        elif j == len(b)-2:
            if b[j] >b[j+1] and b[j-2] and b[j-1]:
                w_c = b[j]=max(b[j-1], b[j+1], b[j-2])
        else:
            if b[j] > b[j-1] and b[j] > b[j-2] and b[j] > b[j+1] > b[j] >b[j+2]:
                w_c = b[j] - max(b[j-2], b[j-1], b[j+1], b[j+2])
    print(f"{i} {w_c}")