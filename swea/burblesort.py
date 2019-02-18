a = [3,5,2,4,7,1]
for i in range(len(a)):
    min = a[i]
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]
print(a)