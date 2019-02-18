def fact(n):
    d = [1,1]
    for i in range(2,n+1):
        d.append(d[i-1]*i)
    return d[n]

c = fact(5)
print(c)
d = fact(10)
print(d)