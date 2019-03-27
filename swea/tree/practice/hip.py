'''
선형 자료구조에서 priority queue 는 선형 자료에서 O(n^2)를 차지해서 이를 대체하기 위해 나온데 힙
힙은 두가지 조건이 맞춰줘야 하는데
 1. 구조적인 모습이 완전 이진트리여야 함(앞에서부터 완전히 채워져야 함)
 2. 내부 논리 모습은 부모의 노드가 자식보다 항상 크거나 작아야 함(일관성)
   최대 힙 : 키 값이 가장 큰 노드를 찾기 위한 완전이진트리
    루트가 가장 큰 값을 가지고 있음.
   최소 힙 : 최대 힙의 반대
   
   삽입, 삭제가 존재하고, 구조를 유지시켜주게 만들어야 하는게 개발자의 숙명

   힙은 프라이어티를 사용하기 위해 사용( Max, Min) 그리고 이제 루트에 있음.
   그렇기에 삭제를 루트에서 진행함.

'''