# 정렬 알고리즘

## 1. 개요

알고리즘 | 평균 수행시간 | 최악 수행시간 | 알고리즘 기법 | 비고
----- | ----- | ----- | ----- | -----
버블정렬 | O(n^2) | O(n^2) | 비교화 교환 | 구현 용이
카운팅 정렬 | O(n+k) | O(n+k) | 비교환 방식 | n이 작을 때 
선택 정렬 | O(n^2) | O(n^2) | 비교와 교환 | 교환의 회수가 버블, 삽입보다 작음 
퀵 정렬 | O(n long n) | O(n^2) | 분할 정복 | 최악의 경우(O(n^2)), 평균적으로 가장 빠르다 
삽입 정렬 | O(n^2) | O(n^2) | 비교화 교환 | n이 작을 때 
병합 정렬 | O(n log n) | O(n log n) | 분할 정복 | 연결리스트의 경우 가장 효율적 

## 2. 구현

### 1) 퀵 정렬

```python
# a는 숫자배열
def quickSort(begin, end):
    if begin < end :
        p = partition(begin, end)
        quickSort(begin, p-1)
        quickSort(p+1, end)
        
def partition (begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L<R :
        while(a[L] < a[pivot] and L<R) : L += 1
        while(a[R] >= a[pivot] and L<R) : R -= 1
        if L < R:
            if L == pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
```

### 2) 선택 정렬

```python
def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[j]
```

### 3) 카운팅 정렬

```python
# A = [1 .. n] # 입력 배열 1 to k
# B = [1 .. n] # 정렬된 배열
# C = [1 .. k] # 카운트 배열

C = [0] * k

for i in range (0, len(B)):
    C[A[i]] += 1

for i in range(1, len(C)):
    C[i] += C[i-1]
    
for I in range (len(B)-1, -1, -1):
    B[C[A[I]]-1] = A[i]
    C[A[i]] -= - 1
```

### 4) 버블정렬

```python
def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```

### 5) 병합 정렬

```python
def merge_sort(m):
    if len(m) <= m:
        return m
    # 1. Div
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]
    # 리스트의 크기가 1이 될 때 까지 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 2. Conquer : 분할 리스트 병합
    return merge(left, right)

# 3. Combine
def merge(left, right):
	result = []
    while len(left) > 0 and len(right) > 0 # 양쪽 리스트에 원소가 남아 있는 경우
    # 두 서브 리스트의 첫 원소들을 비교하여 작은 것 부터 result에 추가
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0 :
        result.extend(left)
    if len(right) > 0 :
        result.extend(right)
    return result
  	
```

