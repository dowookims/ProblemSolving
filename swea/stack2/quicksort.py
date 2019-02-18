def quickSort(a, begin, end):
    if begin < end:
        # p = pivot
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
def partition (a, begin, end):
    #임시 pivot : 맨앞, 맨뒤, 세가지 값의 중간값등 다양함
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L<R): 
            L += 1
        while(a[R] >= a[pivot] and L<R): 
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
        a[pivot], a[R] = a[R], a[pivot]
    return R

a = [4,3,76,23,57,1]
quickSort(a,0,len(a)-1)
print(a)