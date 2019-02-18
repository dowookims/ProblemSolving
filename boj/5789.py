for s in range(1, int(input())+1):
    b,c = list(map(int,input().split()))
    d = ['0']*b
    for i in range(1,c+1):
        l,r = list(map(int,input().split()))
        for q in range(l-1,r):
            d[q] = str(i)
    print(f"#{s} {' '.join(d)}")
