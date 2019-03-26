'''
주어진 배열을 두개로 분할하고 각각 정렬
병합 정렬은 두 부분을 그냥 나누는 반면
퀵 정렬은 분할 시 기준 아이템(pivot)을 중심으로 이보다 작은 건 왼편, 큰건 오른편에 위치
병합이 필요하지 않음
'''

l1 = [11, 45, 23, 81, 28, 34]
l2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
l3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]


def quickSort(aList, l, r):
    if l < r:
        s = partition(aList, l, r)
        quickSort(aList, l, s - 1)
        quickSort(aList, s+1, r)
    return aList


def partition(aList, l, r):
    p = aList[l] #p = pivot value
    i = l
    j = r
    while i <= j:
        while aList[i] <= p and i != r:
            i += 1
        while aList[j] >= p and j != l:
            j -= 1
        if i<j:
            aList[i], aList[j] = aList[j], aList[i]
    aList[l], aList[j] = aList[j], aList[l]

    return j


print(quickSort(l1, 0, len(l1)-1))
