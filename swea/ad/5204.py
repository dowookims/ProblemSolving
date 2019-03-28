import sys
sys.stdin = open("5204.txt", "r")


def merge_sort(aList):
    global res
    lines = len(aList)
    if lines == 1:
        return aList
    m = lines // 2
    left = [0] * m
    right = [0] * (lines - m)


    for i in range(m):
        left[i] = aList[i]

    idx = 0
    for j in range(m, lines):
        right[idx] = aList[j]
        idx += 1

    left = merge_sort(left)
    right = merge_sort(right)
    lm = left[m - 1]
    rm = right[idx - 1]

    if lm > rm:
        res += 1
    return merge(left, right)


def merge(aLeft, aRight):
    ln = len(aLeft)
    rn = len(aRight)
    li = 0
    ri = 0
    rei = 0
    result = [0] * (ln + rn)
    while ln > 0 or rn > 0:
        if ln > 0 and rn > 0:
            if aLeft[li] <= aRight[ri]:
                result[rei] = aLeft[li]
                li += 1
                ln -= 1
            else:
                result[rei] = aRight[ri]
                ri += 1
                rn -= 1
        elif ln > 0:
            result[rei] = aLeft[li]
            li += 1
            ln -= 1
        elif rn > 0:
            result[rei] = aRight[ri]
            ri += 1
            rn -= 1
        rei += 1
    return result


for TC in range(1, int(input())+1):
    res = 0
    N = int(input())
    case = list(map(int, input().split()))
    case = merge_sort(case)
    print('#{} {} {}'.format(TC, case[N//2], res))


for TC in range(1, int(input())+1):
    res = 0
    N = int(input())
    case = list(map(int, input().split()))
    case = merge_sort(case)
    case.sort()
    print('#{} {} {}'.format(TC, case[N//2], res))


for TC in range(1, int(input())+1):
    n = int(input())
    print(f"#{TC} {sorted(input().split())[n//2]}")