## AOE

## AOV

그래프는 차수(degree)가 있다. 정점에 붙어있는 간선의 개수

트리와 그래프가 조금 다른데

무방향 그래프와 방향 그래프에 따라 차수가 다르다.

`간선` 정점을 연결하는 선

`무방향 그래프` => `차수`(정점에 연결된)

`방향 그래프` => `진입차수` `진출차수`

트리는 자식으로 가는 단선만 차수로 따진다. 이를 나중에 자료구조 구성 할 때 따짐



### 위상정렬

1. 진입차수 0을 소거 (방향 그래프)
2. 