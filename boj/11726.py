import sys
a = int(sys.stdin.readline())

d = [0,1,2]
for i in range(3, a+1):
    d.append(d[i-1]+d[i-2])

print(d[a]%10007    )