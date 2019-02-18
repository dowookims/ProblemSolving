# STACK2

###### 2019.02.18

## 계산기

문자열 수식 계산의 일반적 방법은 중위표기법의 수식을 후위 표기법으로 변경한다(스택이용)

### 전위표기법(prefix notation) 

+AB

### 중위 표기법(infix notaiton)

A + B

### 후위 표기법(postfix notation)

AB+

ex) A*B-C/D

* ((A*B) - (C/D)) => ((AB)*(CD)/-) => AB*CD/-



## 백트래킹

해를 찾는 도중에 막히면(해가 아니면) 되돌아가 해를 찾아 가는 기법

최적화 문제와 결정 문제를 해결할 수 있다.

결정 문제 : 문제의 조건을 만족하는 해가 존재하는지 여부를 yes 또는 no로 답하는 문제.

### 백트래킹과 DFS 차이

* 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 그 경로를 따라가지 않음으로 시도의 횟수를 줄임(Prunning, 가지치기)
* 백트래킹은 불필요한 경로를 조기에 차단하고 DFS는 모든 경로를 추적한다

### 풀이법

1. 상태 공간 트리의 DFS 실시
2. 각 노드가 유망한지 점검
3. 그렇지 않으면 부모 노드로 돌아가 검색을 계속한다

### n Queen

### power set

### backtracking을 통한 순열 구하기

## 분할 정복 알고리즘

### 설계기법

완전검색 => 그리디, 백트래킹,(DP), 분할정복

이것들이 탐색공간이 되고, 여기서 논리적이고 체계적으로 탐색공간을 줄여나가는 것.

### 설계 전략

* 분할(Divide) :  해결할 문제를 여러 개의 작은 부분으로 나누고
* 정복(Conquer) : 나눈 작은 문제를 각각 해결한다음
* 통합(Combine) : 필요시 해결된 해답을 모은다.

Do Not Recompute !!

```python
a = 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3
b = 3 * 3 * 3 * 3
c = b * b
# 만약 홀수개라면?
a = 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3
b = 3 * 3 * 3 * 3
c = b * b * 3
```

```python
def Power(Base, Exponent):
    if Exponent == 0 or Base == 0 :
        return 1
    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent/2)
        return NewBase * NewBase
    else :
        NewBase = Power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base
```

이진 검색도 분할정복으로 처리한다.

전제조건 : 정렬이 되어있어야 함.

## 퀵 정렬

```python
def quickSort(a, begin, end):
    if begin < end:
        # p = pivot
        p = partition(a, begin, end)
        queickSort(a, begin, p-1)
        quickSort(a, p+1, end)
def partition (a, begin, end):
    #임시 pivot : 맨앞, 맨뒤, 세가지 값의 중간값등 다양함
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L] < a[pivot] and L<R) : L += 1
        while(a[R] >= a[pivot] and L<R) : R -= 1
        if L < R:
            if L ==pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot
	return R
```

