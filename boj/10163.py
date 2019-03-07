n = int(input())
case = [[0 for _ in range(102)] for _ in range(102)]
count = [0 for _ in range(n+1)]
min_x = 9876
min_y = 9876
max_width = 0
max_height = 0
for i in range(n):
    x, y, w, h = map(int,input().split())

    for r in range(y, y+h):
        for c in range(x, x+w):
            case[r][c] = i+1

for i in range(102):
    for j in range(102):
        if case[i][j]:
            count[case[i][j]] += 1

for i in range(1, len(count)):
    print(count[i])

