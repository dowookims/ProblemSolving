# def solution(arr):
#     d = []
#     for i in range(len(arr)):
#         if i == 0:
#             d.append(arr[i])
#         else:
#             if arr[i] != arr[i-1]:
#                 d.append(arr[i])
#     return d
#
#
# r = solution(a)
# print(r)

a = [1,2,3,4,5,6]
N = 6
visited = [0]*N
t = [0]*N

def perm(k):
    global N
    if k == N:
        print(t)
    else:
        for i in range(N-1):
            if visited[i]:
                continue
            t[k] = a[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0

perm(0)