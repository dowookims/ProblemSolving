def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key :
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

def binarySearch2(a,low, high, key):
    if low > high :
        return False
    else :
        middle = (low + high) //2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        else:
            return binarySearch2(a, middle+1, end, key)
    

a = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(a,6))
print(binarySearch2(a,1,10,6))