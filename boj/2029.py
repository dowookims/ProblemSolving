a = int(input())
for i in range(1,a+1):
    b,c = list(map(int, input().split()))
    print(f"#{i} {int(b/c)} {b%c}")