for i in range(1, 11):
    a = int(input())
    b = list(map(int, input().split()))
    b.append(0)
    b.append(0)
    b.insert(0,0)
    b.insert(0,0)
    w_c = 0
    for j in range(2,len(b)-2):
        c = max(b[j-2], b[j-1], b[j+1], b[j+2])
        if b[j] > c:
            w_c += b[j]-c
    print(f"#{i} {w_c}")