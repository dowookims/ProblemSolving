'''
여러개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
자료를 최소 단위의 문제까지 나눈 후 차례대로 정렬하여 최종 결과 겟
top - down
O(nlogn)
'''

l1 = [11, 45, 23, 81, 28, 34]
l2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
l3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def merge_sort(aList):
    n = len(aList)
    if n == 1:
        return aList
    m = n // 2
    left = aList[0:m]
    right = aList[m:n]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(aLeft, aRight):
    result = []

    while len(aLeft) > 0 or len(aRight) > 0:
        if len(aLeft) > 0 and len(aRight) > 0:
            if aLeft[0] <= aRight[0]:
                result.append(aLeft.pop(0))
            else:
                result.append(aRight.pop(0))
        elif len(aLeft) > 0:
            result.append(aLeft.pop(0))
        elif len(aRight) >0:
            result.append(aRight.pop(0))
    return result

print(merge_sort(l1))
print(merge_sort(l2))
print(merge_sort(l3))

