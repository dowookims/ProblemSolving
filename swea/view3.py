a = int(input())
for i in range(1, a+1):
    b = list(map(int,input().split()))
    new_b = b.insert(0,0)
    new_b = b.insert(0,0)
    new_b = b.insert(len(b)-1,0)
    new_b = b.insert(len(b)-1,0)
    w_c = 0
    for j in new_b:
        if new_b[j] > new_b[j-1] and new_b[j] > new_b[j-2] and new_b[j] > new_b[j+1] > new_b[j] >new_b[j+2]:
            w_c = new_b[j] - max(new_b[j-2], new_b[j-1], new_b[j+1], new_b[j+2])
    print(f"{i} {w_c}")