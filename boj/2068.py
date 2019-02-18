a = int(input())
for i in range(1, a+1):
    c = max(list(map(int, input().split())))
    print(f"#{i} {c}")