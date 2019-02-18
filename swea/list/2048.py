a = 5
c = [[0 for _ in range(a)] for _ in range(a)]
a = [
    [4,8,2,4,0],
    [4,4,2,0,8],
    [8,0,2,4,4],
    [2,2,2,2,8],
    [0,2,2,0,0]
]
for i in range(len(a),0,-1):
    for j in range(len(a)):
        if a[i][j] == a[i-1][j]:
            a[i-1][j] = a[i-1][j]*2
            a[i][j] = 0
print(a)