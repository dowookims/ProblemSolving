n = int(input())
case = [0]*n
for i in range(n):
    case[i] = list(map(int, input().split()))
for item in case:
    print(item)