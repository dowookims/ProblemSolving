def solution(arr):
    d = []
    for i in range(len(arr)):
        if i == 0:
            d.append(arr[i])
        else:
            if arr[i] != arr[i-1]:
                d.append(arr[i])
    return d

a = [4,4,4,3,3]
r = solution(a)
print(r)