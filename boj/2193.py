'''
이친수
0으로 시작하지 않고
1이 두번 연속으로 나타나지 않음
'''

n = int(input())
d = [0, 1, 1]
if n >=3:
    for i in range(3, n+1):
        d.append(d[i-1]+d[i-2])
print(d[n])

