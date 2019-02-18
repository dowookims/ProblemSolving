'''
가장 긴 증가하는 부분 수열
수열 크기 N과
수열 A가 주어짐
'''
N = int(input())
A = list(map(int, input().split()))
d = [0]*1001
c = 0
for i in range(len(A)):
    if d[A[i]] == 0:
        d[A[i]] = 1
        c += 1

print(c)

