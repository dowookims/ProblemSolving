# Queue

###### 19.02.25 Monday

* FIFO(First In First Out) 구조를 가진다.

```
_____________________________________
|  |  |  |  |  |  |  |  |  |  |  |  |
-------------------------------------
Front							rear
inqueue : 맨 뒤에 데이터를 넣는다
dequeue : 맨 앞에 데이터를 pop한다
isEmpty() : underflow
isFull() : 큐가 포화인지
Qpeek() : 큐의 앞쪽에서 원소를 삭제 없이 반환
```

![queue1](/img/q1.png)

![queue2](/img/q2.png)

![queue3](/img/q3.png)

***

## 선형큐

### 1차원 배열을 이용한 큐

* 큐의 크기 = 배열의 크기
* 초기 상태 : front = rear = -1
* 공백 상태 : front = rear
* 포화 상태 : rear = n-1(n : 배열의 크기, n-1 : 배열의 마지막 인덱스)

### 큐의 구현

* 크기 n인 1차원 배열 생성

* front와 rear를 -1로 초기화

* 삽입 : enQueue(item)

* ```python
  def enQueue(item):
  	global rear
  	if isFull() : print("Queue_Full")
  	else :
  	    # rear 값을 하나 증가시켜 새로운 원소 삽입할 자리 마련
           # 그 인덱스에 해당하는 배열원소에 item 저장
  		rear = rear + 1;
  		Q[rear] = item
  ```

* 삭제 : deQueue()

* ```python
  def deQueue():
  	if(isEmpty()) then Queue_Empty();
      else {
          front += 1
          return Q[front];
      }
  ```

* 공백상태 : front = rear

* 포화상태 : rear = n-1

* ```python
  def isEmpty():
      return Front == rear
  def Full():
      return rear == len(Q)-1
  def Qpeek():
      if isEmpty() : print("Queue_Empty")
      else : return Q[front+1]
  ```
```python
class Queue():
    
    def __init__(self):
        self.q = [0]*10000
        self.front = -1
        self.rear = -1
    def enQueue(self, n):
        self.rear += 1
        self.q[self.rear] = n
    def deQueue(self):
        self.front += 1
        return print(self.q[self.front])

    def isEmpty(self):
        return self.front == self.rear


    def isFull(self):
        return self.rear == len(self.q)-1
    
    def qPeek(self):
        if self.isEmpty() : print("Queue_EMpty")
        else : return self.q[self.front+1]
```

***

### 선형 큐 이용시 문제점

포화 상태시 인식하여 더 이상 삽입을 못하게 됨

* 해결방안 1

  매 연산이 이루어질 때 저장된 원소들의 배열의 앞부분으로 모두 이동시킴 : 원소 이동에 많은 시간이 소요되어 효율성이 떨어짐

* 해결방안2 : Circular Queue

  1차원 배열 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하여 사용

### 원형 큐의 구조

* 초기 공백 상태
  * front = rear = 0
* Index의 순환
  * front 와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0 으로 이동
  * 이를 위해 mod 사용

![q4](/img/q4.png)




```python
class Queue():
    def __init__(self,n):
        self.queue = [0]*n
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return (self.rear+1) % len(self.queue) == self.front
    
    def enQueue(self, item):
        if self.isFull():
            print("Queue Full")
        else:
            self.rear = (self.rear+1) % len(self.queue)
            self.queue[self.rear] = item
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            self.front = (self.front + 1) % len(self.queue)
            return self.queue[self.front]
```

시작과 끝의 구분을 해주기 위해 원형큐에서는 front에 위치한 값은 비워둔다.

***

## 연결큐(Linked Queue)

큐의 원소 : 단순 연결 리스트의 노드

큐의 원소 순서 : 노드의 연결 순서. 링크로 연결 됨

front : 첫 번째 노드를 가리키는 링크

rear : 마지막 노드를 가리키는 링크

* 상태표현
  * 초기 상태 : front = rear = null
  * 공백 상태 : front = rear = null

![q5](/img/q5.png)

![q6](/img/q6.png)

주소값을 따라가면서 연결해줘야 하기 때문에 주소 값을 넣고 변경하는 작업이 들어가야 한다.

![q6](/img/q7.png)

파이썬에서는 객체의 id 값을 주면서 이동하는 방식으로.

객체지향 언어에서는 id가 객체 instance의 값

```python
class Node:
    def __init__(self,item, n=None):
        self.item = item
        self.next = n

class LinkedQueue:
    def __init__(self,n):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    def enQueue(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.front = newNode
        else :
            self.rear.next = newNode
        self.rear = newNode
    
    def deQueue(self):
        if self.isEmpty():
            print("Queue Empty")
            return None
        item = self.front.item
        self.front = self.front.next
        if self.isEmpty():
            self.rear = None
        return item
    
a = LinkedQueue(10)
a.enQueue(5)
a.enQueue(4)
a.enQueue(3)
print(a.deQueue())
print(a.deQueue())
print(a.deQueue())
```

## 우선순위큐(Priority Queue)

### 우선순위 큐의 특성

* 우선순위를 가진 항목들을 저장하는 큐
* FIFO가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다

### 우선순위 큐의 적용 분야

* Simulation System
* Network Traffic Control
* OS Task Scheduling

### 우선순위 큐의 구현

* 배열을 이용한 우선순위 큐
* 리스트를 이용한 우선순위 큐

### 우선순위 큐의 기본 연산

* 삽입 : enQueue
* 삭제 : deQueue

![q8](/img/q8.png)

### 배열을 이용한 우선순위 큐

#### 1. 배열을 이용하여 우선순위 큐 구현

* 배열을 이용하여 자료 저장
* 원소 삽입 과정에서 우선순위 비교하여 적절한 위치에 삽입
* 가장 앞에 최고 우선순위 원소 위치

#### 2. 문제점

* 배열 사용하므로 삽입이나 삭제 연산이 일어날 때 원소의 재배치 발생
* 이에 소요되는 시간이나 메모리 낭비가 큼

```
I/O 의 기본:
  * Standard Input
  * Standard Output
  * Standard Error
```



### 큐의 활용 : Buffer

#### 버퍼

* 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 데이터 보관하는 메모리 영역
* 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다

#### 버퍼의 자료 구조

* 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
* 순서대로 입력 / 출력 / 전달되야 하므로 큐가 활용 됨
* 시스템이 사용하는 큐가 버퍼라고 사용된다고 볼 수 있다.

***

## BFS(Breadth First Search)

그래프를 탐색하는 두가지 방법 : DFS, BFS

BFS는 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후 방문했던 정점을 시작점으로 다시 인접한 정점들을 차례로 방문

인접한 정점들에 대해 탐색 후 차례로 다시 BFS를 진행해야 하므로 큐를 활용함

DFS는 Stack, BFS는 Queue를 구현해서 함

![q9](/img/q9.png)

![q10](/img/q10.png)

