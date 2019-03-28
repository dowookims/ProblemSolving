'''
5205. quickSort
find n//2
'''
import sys
sys.stdin = open("5205.txt", "r")


# def quickSort(aList, l, r):
#     if l < r:
#         s = partition(aList, l, r)
#         if s == len(aList)//2:
#             return
#         quickSort(aList, l, s - 1)
#         quickSort(aList, s+1, r)
#     return aList
#
#
# def partition(aList, l, r):
#     p = aList[l]
#     i = l
#     j = r
#     while i < j:
#         while aList[i] <= p and i < r:
#             i += 1
#         while aList[j] >= p and j > l:
#             j -= 1
#         if i<j:
#             aList[i], aList[j] = aList[j], aList[i]
#     aList[l], aList[j] = aList[j], aList[l]
#
#     return j



# def quickSelection(arr, l, r ,k):
#     i = l
#     j = r
#
#     while j != k:
#         while i < j:
#             while i <= r and arr[i] <= arr[l]:
#                 i += 1
#             while arr[j] > arr[l]:
#                 j -= 1
#             if i < j:
#                 arr[i], arr[j] = arr[j], arr[i]
#             arr[l], arr[j] = arr[j], arr[l]
#
#             if j < k:
#                 l = j +1
#             else:
#                 r = j - 1
#     return arr[j]

for TC in range(1, int(input())+1):
    N = int(input())
    case = list(map(int, input().split()))
    z = quickSelection(case, 0, len(case)-1, len(case) //2)
    r = N//2
    print(case)
    print('#{} {}'.format(TC, z))