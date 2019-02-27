# List(LinkedList)

###### 2019.02.27 WED

## List

* 순서를 가진 데이터의 집합을 가리키는 추상 자료형

* 데이터 중복 허용

### 1. 종류

#### 1) 순차 리스트 

* 배열 기반으로 구현 (논리적으로 메모리상 근접해 있음)
* 순차리스트 구현시 삽입 / 삭제 연솬 과정에서 연속적인 메모리 배열을 위해 원소를 이동 시키는 작업이 필요
* 원소의 개수가 많고, 삽입 삭제가 빈번하게 일어나면 작업에 소요되는 시간이 크다
* 배열 크기가 정해져 있을 경우 과 할당하여 메모리 낭비를 초래할 수도 있고, 초과시 새로 배열을 만들어야 해서 비효율적일 수 있음

#### 2) 연결 리스트 : 메모리의 동적할당을 기반으로 구현
* 자료의 논리적인 순서와 메모리 상 물리적인 순서가 일치하지 않고 개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룬다.

* 링크를 통해 원소에 접근하므로 순차 리스트에서 처럼 물리적인 순서를 맞추기 위한 작업이 필요하지 않다

* 자료구조의 크기를 동적으로 조정할 수 있어 메모리의 효율적 사용 가능

### 2. 기본 구조

#### 1) 노드
    * 연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료 단위
    * 데이터 필드와 링크 필드를 가지고 있음
#### 2) 헤드
    * 리스트의 처음 노드를 가리키는 레퍼런스

### 3. 연결 구조
    * 노드가 하나의 링크 필드에 의해 다음 노드와 연결되는 구조를 가짐
    * 헤드가 가장 앞의 노드를 가리키고, 링크필드가 연속적으로 다음 노드를 가리킴
    * 최종적으로 NULL을 가리키는노드가 리스트의 가장 마지막 노드

### 3. 주요 함수

  * Node
  ```python
class Node:
    def __init__(self, data, next = None)
        self.data = data
        self.next = next
  ```
  * addToFirst() 
  ```python
def addToFirst(data):
    global Head
    Head = Node(data, Head)
  ```
  * addToLast()
  ```python
def addToLast(data):
    global Head
    if Head == None :
        Head = Node(data)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data)
  ```
  * add
  ```python
def add(pre, data): #pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else :
        pre.link = Node(data, pre.link)
  ```
  * delete()
  ```python
def delete(pre):
    if pre == None or pre.link==None:
        print('error')
    else :
        pre.link = pre.link.link
  ```
  * get()
  ```python

  ```

  

## Doubly Linked List

### 1. 특성

* 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
* 두 개의 링크필드와 한 개의 데이터 필드로 구성

### 2. 연결 구조

![L1](C:\Users\student\ProblemSolving\swea\list1\img\l1.png)

