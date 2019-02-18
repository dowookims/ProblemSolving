a = int(input())
for i in range(1,a+1):
    b,c = list(map(int, input().split()))
    if b>c:
        print(f"#{i} >")
    elif b==c:
        print(f"#{i} =")
    else:
        print(f"#{i} <")