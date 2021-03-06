# STACK

### 스택의 특성

물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조

스택에 저장된 자료는 선형 구조를 갖는다.

`LIFO(Last-In-First-Out)` 후입선출.

- 선형구조 : 자료간 관계가 1:1
- 비선형 구조 : 자료간 관계가 1:n (트리)

스택에 자료를 삽입하거나 꺼낼 수 있다.

마지막에 삽입한 자료를 가장 먼저 꺼낸다. 

### 자료구조

선형으로 저장할 저장소. 주로 배열에서 작업을 한다.

### 연산

- push
- pop
- isEmpty
- peek

### 고려사항

1차원 배열을 사용하여 구현할 경우 구현이 용이하나 스택의 크기를 변경하기 어렵다

저장소를 동적 할당하여 스택을 구현할 수 있는데, 동적 연결리스트를 이용하여 구현한다.

구현은 복잡하나, 메모리를 효율적으로 사용할 수 있다.

***

##  Memoization

캐싱하여 실행속도를 빠르게 하는 기술로 DP(Dynamic Planning)의 핵심이 되는 기술

피보나치를 recursive로 구현하면 O(2^N)이나 memoization을 활용하면 실행시간을 O(N)으로 줄일 수 있다.

***

# Dynamic Programming(DP)

그리디 알고리즘과 같이 `최적화 문제`를 해결하는 알고리즘

입력 크기가 작은 부분 문제들을 해결한 후 그 해를 이용하여 큰 크기의 부분 문제를 해결하여 주어진 입력 문제를 해결하는 알고리즘



`최적화 문제`, `카운팅 문제`등에 사용된다.

동적계획법은 문제를 부분 문제들로 분할하고 부분 문제의 solution을 구해서 더 큰 부분 문제의 해를 구하는 방법이지만 많은 하위문제들이 중복해서 계산되면 비용이 많이 듬

 	1. 부분 문제들의 solution 저장(memoization)
 	2. 이를 사용

### 그래프 해석

1. 재귀 알고리즘은 주어진 문제에 대한 부분 문제 그래프로 볼 수 있다(재귀 호출 트리)
2. 알고리즘이 항상 종료되면 하위 문제 그래프는 비순환적(acyclic) DAG 혹은 트리
3. 자연스러운 재귀작업, 하위문제 그래프의 비메모리(memoryless) 순회와 같다
4. 부분 문제에 n 개의 경로가 있다면 n번의 해를 구하는 작업을 하므로 지수적(exponentially로 많은 결로를 가질 수도 있음)
5. 부분 문제 간 의존성 파악

### 반복적 DP

부분 문제간 의존성(선행 관계)를 파악후 부분 문제 그래프를 DAG 그래프로 간주하고 역 위상 정렬을 한다.



### 동적계획법 적용하기

* 부분 문제 정의 => 쪼개기
* 부분 문제간 관계 찾기 => 재귀적으로 해를 구하거나 더 작은 문제들의 solution으로 큰 문제 표현
* 기저 사례 찾아서 해결(base)
* 상향식으로 문제를 해결하는 방법을 찾는다.
* bottom-up
* 부분 문제들이 서로 overlapping된다
* 분할 정복의 경우 연관 없는 부분 문제들로 분할되며 Top-down 방식

***

# DFS

## 상태 공간 트리(State Space Tree(Graph))

해를 찾는 과정을 상태 공간 트리(그래프)로 표현한다.

이는 Backtracking과정에서 나오는데, 

Backtracking은 여러가지 선택지들 중 일련의 선택(결정)을 해야하는 상황에서

* 어떤 선택을 해야하는지 충분한 정보가 없으며

* 하나의 선택이 새로운 선택지를 만들때

* 일련의 선택들은 문제에 대한 해(solution)이 가능할 때

* 가능한 경우들을 문제의 상태 공간이라고 한다.

SST에서는

- 루트 노트(시작 정점)은 초기 상태가 되며
- 하나의 노드는 하나의 상태를 나타내며
- 각 노드는 자식 노드수 만큼 가능한 선택지가 존재하며
- 단말 노드는 더이상 선택지(경로) 가 없음을 의미하며
- 완전 탐색인 경우 하나의 단말노드에 이르는 경로는 하나의 후보해가 된다.

`백트래킹`은 탐색 공간의 모든 가능한 상태를 조사하는 체계적인 방법으로

* 하나의 해는 순서를 가지는 선택들의 집합으로 표현되며
* 일반적으로 재귀로 구현되며
* 어떤 시점까지의 선택들을 추적할 수 있어야 한다.
  * 지금까지의 경로를 저장한다(Memoization)
  * 현재 선택을 취소하고 이전의 선택으로 되돌아 갈 수 있어야 한다.

### 가지치기

탐색 공간을 줄여서 해를 더 빠르게 찾기 위해 가지치기(Prunning)을 수행할 수 있는데,

SST를 탐색하는 과정에서 현재 노드가 solution에 이르는 경로에 포함되는지 판단한다.

