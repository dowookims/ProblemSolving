arr = [3,6,7,1,5,4]

n = len(arr)
a = 0
for i in range(1<<n):
    for j in range(n+1):
        if i & (1<<j):
            print(arr[j], end=", ")
    print()
    a+=1
print(a)