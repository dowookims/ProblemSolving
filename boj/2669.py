'''
2669 직사각형 네개의 합집합의 면적 구하기
'''

case = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            case[r][c] = 1
res = 0
for r in range(1,101):
    for c in range(1,101):
        if case[r][c]:
            res += 1
print(res)
