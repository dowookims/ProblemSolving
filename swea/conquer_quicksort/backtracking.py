'''
여러 가지 선택지들이 존재하는 상황에서 한가지 선택
선택이 이루어지면 새로운 선택지들의 집합이 생성
이런 선택을 반복하여 최종 상태에 도달
올바른 선택을 계소갛면 목표 상태에 도달함.
ex) 당첨 리프 노드 찾기

백트래킹과 DFS 차이
어떤 노드에서 출발하는 경로가 해결채긍로 이어질거 같지 않으면 그경로를 따라 가지 않음으로 시도의 횟수 줄임(가지치기, 플러닝)
깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
DFS로 탐색하기에 경우의 수가 많음, N!
백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어드나 최악의 경우 지수함수 시간을 요함

루트 노드에서 리프 노드 까지의 경로는 해답후보가 되는데 깊이 우선 검색을 하여 그 해답후보 중에서 해답을 찾을 수 있다.
그러나 이 방법을 사용하면 해답이 될 가능성이 전혀 없는 노드의 후손노드들도 모두 검색해야 하므로 비효율적이다.

백트래킹은 어떤 노드의 유망성을 점검한 후 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며 반대로 해답의 가능성이 있으면 유망
가지치기: 유망하지 않는 노드가 포함되는 경로는 더이상 고려하지 않는다

절차:
상태 공간 트리의 깊이 우선 검색 실시
각 노드가 유망한지 점검
그렇지 않으면 노드의 부모 노드로 돌아가 검색 진행
'''