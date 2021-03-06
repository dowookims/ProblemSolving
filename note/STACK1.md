# 190211 STACK

* LIFO 구조
* 스택에 저장된 자료는 선형 구조를 갖는다
  * 선형구조 : 자료간 관계가 1대1의 관계
  * 비선형구조 : 자료 간의 관계가 1대 N의 관계를 갖는다.

```
ADT(Abstract Data type) STACK
- 논리적 구조 : LIFO
- 연산 : 삽입(push), 삭제(pop), 출력(peek, pop), 공백 확인(isEmpty)
```

이를 선택, 구현하는게 중요하다.

시작시 맨 처음에는 TOP이 -1을 가르키게 한다(공백) 이후 `증가(push)`에는

	1. TOP을 하나 증가 시키고
	2. 값을 위치 시킨다.(저장한다.)
	3. All operations are O(1).

꺼내는 연산인 `pop`은 TOP이 정보를 가지고 있기 때문에

	1. TOP의 값을 return 하고
	2. TOP을 하나 감소 시킨다.

Size와 TOP이 같을 때, 더 추가하면 `Stack Over Flow`발생, 이를 방지하는 로직을 구성해야함.

파이썬의 경우 메모리 동적할당이 되기 때문에 적당한 크기를 조절하면 되지만, 위험할 때가 존재한다.

STACK이 비었을 때 Pop 실행시 `Under Flow`발생. 즉, TOP이 Initial(Empty) 상태 일 때 더이상 꺼낼 수 없다는 것을 제어 해 줘야 한다.

## OS 상에서 STACK 구현 시 주의 사항

원래 배열의 크기는 정해져 있으므로, 그 정해진 크기만큼 배열이 값을 할당할 수 있다. 여기서 append(push)를 통해서 배열을 구현 할 경우, 추가적으로 자료 공간을 할당 받고 이를 추가해야 하는데, 연속되는 메모리 공간을 OS에 요청해서 추가적으로 공간을 확보 한 후 이 공간에 복사를 한다. 그렇기에 문제가 발생함.

```python
#1
loo = 100000000
s = []
for i in range(loo):
    s.append(i)
#2
s = [0] * loo
for i in range(loo):
    s[i] = i
print("okok")
# 1 은 메모리 문제로 에러가 나고
# 2 는 문제없이 잘된다.
'''
append는 메모리 공간을 직접 관리하지 않기 때문에 수천만개의 데이터를 append할시 메모리 에러가 날 수 있으나
index를 통한 직접 접근은 이런 에러가 나타나지 않으며, append보다 빠르게 처리 할 수 있다.
'''

```

```python
stack = [0] * 10
top = -1

for i in range(3):
    top += 1
    stack[top] = i
    
for i in range(3):
    t = stack[top];
    top -= 1
    print(t)
```

STACK의 사용

 	1. 괄호가 잘 닫혀 있나용?
 	2. function call
 	3. recursive call => Base case 잡는게 중요하다

상태공간 트리 => 탐색공간 완전검색 => 논리적으로 중복된 공간, 회피해야할 공간을 정해서 탐색 공간을 줄이는것 !

그래서 중복을 줄이는 방법중 하나가 메모를 하는것. 메모지에이션

여기서 param과 value를 메모하는데, param이 integer 하나면, 1차 배열로 한다.

param이 두개면 2차 배열로 가서 작업을 진행한다. 이건 테크닉.



재귀 호출시, 피보나치 수열을 구할 때 재귀함수로 구현할 경우 엄청난 중복 호출이 존재한다. 그래서 피보나치 수열의 경우 시간복잡도 O = 2^n 을 가지게 되는데

`메모이제이션(memoization)`은 프로그램 실행시 이전에 계산한 값을 메모리에 저장해서 다시 계산하지 않도록 하여 실행속도를 빠르게 하는, `동적 계획법`의 핵심이 되는 기술

그래서 실행시간을 O(n)으로 만들 수 있다.

```python
def fibo(n):
    memo = [0,1]
    if n >= 2 and len(memo) <= n :
        memo.append(fibo1(n-1) + fibo(n-2))
    return memo[n]
```

## DP(Dynamic Programming / Dynamic Planning)

동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘

먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘

## DFS(Depth First Search)

자료구조는 선형자료구조와 비선형 자료구조(Tree, Graph)가 있다.

선형자료구조 : 1:1 / 비선형구조 : 1:n

트리는 그래프의 부분집합이다. 그리고 이 둘의 표현법을 반드시 알아둬야 한다.

이를 구현하기 위해 인접행렬과 인접 리스트 구조가 있다.

`인접행렬` 6 x 6

|      | 1    | 1    |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 1    |      |      | 1    | 1    |      |
| 1    |      |      |      |      | 1    |
|      | 1    |      |      |      |      |
|      | 1    |      |      |      |      |
|      |      |      |      |      |      |

=> 메모리 낭비와 시간 소모가 많다

`인접 리스트`

비선형 구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요한데

* 깊이 우선 탐색(DFS) : Stack
  * 사용자 정의 stack
  * 시스템 정의 stack(재귀) => 가끔 performance가 딸리고, stackoverflow가 발생
* 너비 우선 탐색(Breadth First Search) : Queue
* 자기를 처리하고, 이웃 정보를 처리한다. 이를 Stack이나 Queue에
* 무방향 그래프는 인접행렬 x,y / y,x 축에 다 값을 넣고
* 방향 그래프는 x,y에다가만 넣자

최단경로 : BFS / 다익스트라, 벨만포드, 플로이드, 순열 iDP

MST(Minimum spanning Tree)

***

DFS 알고리즘

1) 시작 정점 v를 결정하며 방문

2) 정점 v에 인접한 정점 중에서

​	-1 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push, 정점 w를 방문 그리고 w를 v로 하여 다시 2)를 반복

​	-2 방문하지 않은 정점이 없으면 탐색의 방향을 바꾸기 위해 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복

3) 스택이 공백할 때 까지 2를 반복

```python

```

