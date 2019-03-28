# 완전 검색 & 그리디

## 1. 반복(Iteration) 과 재귀(Recursion)

### 설명

* 반복과 재귀는 유사한 작업을 수행할 수 있다.
* 반복은 수행하는 작업이 완료될 때 까지 계속 반복하며
* 재귀는 주어진 문제의 해를 구하기 위해 동일 하며 더 작은 문제의 해를 이용하는 방법
* 즉, 재귀는 하나의 큰 문제를 해결할 수 있는 (해결하기 쉬운) 작은 문제로 쪼개고 결과를 결합

### 재귀적 알고리즘

* 재귀적 정의는 두 부분으로 나뉘는데
  * 하나 또는 그 이상의 기본 경우(basic case or rule)
    * 집합에 포함되어 있는 원소로 induction(귀납법)을 생성하기 위한 seed 역할
  * 하나 또는 그 이상의 유도된 경우(inductive case or rule)
    * 새로운 집합의 원소를 생성하기 위해 결합되어지는 방법

' backtacking + preprocessing + pruning + greedy'

' backtacking + preprocessing + pruning'

'backtracking + pruning'

'backtracking + dynamic programming'

'전자카트 => 미리 줬네 / 최적 거리 => 만들어서 하장'