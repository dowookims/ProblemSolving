# 트리

* 비선형 구조
* 그래프의 일종
* 원소들 간에 1:n 관계를 가지는 자료구조
* 원소들 간에 계층관계를 가지는 계층형 자료구조
* 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조

## 1. 정의

* 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다

  * 노드 중 최상위 노드를 루트라 한다
  * 나머지 노트들은 n(>=0) 개의 분리 집합 T1...TN으로 분리 될 수 있다

* 이들 T1, ... TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 한다.

![tree](/img/t1.png)

  

## 2. 용어정리

- leaf Node(단말 노드) : 제일 하위에 존재하는 노드
- 부모 노드, 자식 노드 : 상위 노드와 하위 노드를 가리킨다.
- 노드(node) : 트리의 원소
- 간선(edge) : 노드를 연결하는 선. 부모 노드와 자식 노드 연결
- 루트 노드(root node) : 트리의 시작 노드
- 형제 노드(sibling node) : 같은 부모 노드의 자식 노드들
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 차수
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중 가장 큰 값
  - 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드
- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중 가장 큰 값. 최대 레벨

![tree](/img/t2.png)

![tree](/img/t3.png)

## 3. 이진트리

* 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리

* 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리

![binary_tree](/img/t4.png)

* 레벨 i에서의 노드의 최대 개수는 2^i

* 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 h+1, 최대 개수는 2^(h+1) -1

### 3-1 이진 트리의 종류

#### 1) 포화 이진 트리(Full Binary Tree)

* 모든 레벨에 노드가 포화 상태로 차 있는 이진 트리
* 높이가 h 일 때, 최대의 노드 개수인 2^(h+1)-1의 노드를 가진다
* 루트를 1번으로 하여 2^(h+1)-1까지 정해진 위치에 대한 노드 번호를 가진다.

![Full Binary Tree](/img/t5.png)

#### 2) 완전 이진 트리(Complete Binary Tree)

* 높이가 h, 노드의 수가 n일 때 ( 단 h+1 <= n < 2^(h+1)-1), 포화 이진 트리의 노드 번호 1부터 n 까지 빈 자리가 없는 이진 트리

![Complete Binary Tree](/img/t6.png)

#### 3) 편향 이진 트리(Skewed Binary Tree)

* 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만 가진 이진 트리
* 왼쪽 편향 이진 트리, 오른쪽 편향 이진 트리

![Skewed Binary Tree](/img/t7.png)

### 3-2) 순회(Traversal)

* 트리의 각 노드를 중복되지 않게 전부 방문 하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다

* 순회는 트리의 노드를 체계적으로 방문하는 것으로 3가지 방법이 있는데

  * 전위순회(Preorder Traversal) : VLR

    * 부모노드 방문 후 자식 노드를 좌,우 순서로 방문

    * 현재 노드 n을 방문하여 처리 => V

    * 현재 노드 n의 왼쪽 서브트리로 이동 => L

    * 현재 노드 n의 오른쪽 서브트리로 이동 => R

      ```python
      def preorder_traverse(T):
          if T:
              visit(T)
              preorder_traverse(T.left)
              preorder_traverse(T.right)
      ```

      ![preorder traversal](/img/t8.png)

      

  * 중위순회(Inorder Traversal) : LVR

    * 왼쪽 자식, 부모, 오른쪽 자식 노드 순

    * 수행 방법

      * 현재 노드 n의 왼쪽 서브 트리로 이동 => L
      * 현재 노드 n을 방문하여 처리 => V
      * 현재 노드 n의 오른쪽 서브 트리로 이동 => R

      ```python
      def inorder_traverse(T):
          if T:
              inorder_traverse(T.left)
              visit(T)
              inorder_traverse(T.right)
      ```

      ![inorder traversal](/img/t9.png)

      

  * 후위순회(Postorder Traversal) : LRV

    * 자식노드를 좌우 순서로 방문 후 부모 노드 방문

    * 수행 방법

      * 현재 노드 n의 왼쪽 서브트리로 이동 : L
      * 현재 노드 n의 오른쪽 서브트리로 이동 : R
      * 현재 노드 n 방문 처리 : V

      ```python
      def postorder_traversal(T):
          if T:
              postorder_traverse(T.left)
              postorder_traverse(T.right)
              visit(T)
      ```

      ![postorder_traversal](/img/t10.png)

***

![p1](/img/t11.png)

1. A B D E H I J C F K G  L M
2. H D I B J E A F K C L G M
3. H I D J E B K F L M G C A

***

### 3-3 이진 트리의 표현

![rep](/img/p1.png)

![p2](/img/p2.png)

자식 노드를 찾아 가려면 부모 노드 i 에서 i * 2 or i * 2 + 1

부모 노드를 찾아 가려면 자식 노드에서 i //2

그러나 이는 FBT에서만 가능, SBT에서는 낭비가 크다.

* 배열을 이용한 이진 트리의표현의 단점은
  * 편향 이진 트리의 경우 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  * 트리의 중간에 새로운 노드 삽입, 기존 노드 삭제시 배열 크기 변경이 어려워 비 효율적

#### 그래서 LinkedList를 사용

* 배열을 이용한 Binary Tree 표현 단점을 보완하기 위해 Linked List를 이용하여 Tree 표현

![LinkedLIst Tree](/img/lt1.png)

![LinkedList Tree](/img/lt2.png)

***

## 이진트리를 활용한 수식 트리

### 수식을 표현하는 이진 트리

* 수식 이진 트리(Expression Binary Tree)라고 부르기도 함
* 연산자는 루트 노드이거나 가지 노드
* 피연사자는 모두 잎 노드

![expression binary tree](/img/e1.png)



