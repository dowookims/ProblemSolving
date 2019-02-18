t = int(input())
for i in range(1,t+1):
    n = int(input())
    print(f"#{i} {int(n**(1/3) if int(n**(1/3)) == n**(1/3) else -1)}")