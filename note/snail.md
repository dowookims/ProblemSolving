# 2019/01/22

## 달팽이 수열

* 선형 자료구조에서 min max 찾는법은 min , max를 첫번째 값으로 하고, 확장하면서 계속 갱신해 나가는 것.
* 행 우선 순회로 min 값을 구함
* is wall : 벽에 부딪히면(index out of range) 방향을 전환하는 함수를 만들어줌
* 여기서 추가적으로 조사하는 값 이외에 0과 다른 값이 존재해도 벽이라고 생각
* 방향 전환을 어떻게 할 것인가? 선생님은 delta를 만들어서 사용
* ㅁ 안에 ㅁ 식으로 재귀로 풀 수도 있다.

```python
ary [[9,20,2,18,11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14]]

#빈배열 생성
sorted_ary = [[0 for _ in range(5)] for _ in range(5)]

#최소값 구하는 함수(Selection Sort)
del sel_min():
    minX, minY = 0, 0
    for i in range(5):
        for j in range(5):
            if ary[minX][minY] > ary[i][j]:
                minX, minY = i, j
                
    min = ary[minX][minY]
    # 최소값을 구한 후 마킹을 함으로써 이미 바뀌었다고 표시
    ary[minX][minY] = 99
    return min

# 벽 함수
def isWall(x,y):
    if x < 0 or x >= 5  : return True
    if x < 0 or y >= 5: return True
    if sorted_ary[x][y] != 0: return True
    return False

X, Y = 0, 0
#dx, dy는 벽을 만나면 좌표를 통해 방향을 바꾸는 함수.
dx = [0,1,0-1]
dy = [1,0,-1,0]
dir_stat = 0 # 0 오른쪽 1 아래 2 왼쪽 3위

for i in range(25)
	cur_min = sel_min()
    sorted_ary[X][Y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]
    
    if isWall(X,Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        
        # dx, dy의 out of range error 방지하기 위해서
        dir_stat = (dir_stat +1) %4
        X = X +dx[dir_stat]
        Y = Y + dy[dir_stat]

# 출력함수
               
```

```
Solving Club List2 문제 4개 풀이
다음에 Solving Club 추가 5문제
별이 5개

List2 문제 4개 메일로 보내기

	1. 해당날의 과제는 항상 자정까지
	2. 메일 제목을 서울1반날짜이름 형식으로
	3. 파일 제목도 이 형식 그대로
	4. 주석
	5. 미완은 점수에 안들어간다. => 안보내도 됨(pass 된 것만)
	6. 코드 지도는 보내도 된다.
	
	소스는 평이하게 짤 것(옵티멀하게 짜지 않아도 됨(축약 ㄴㄴ))
```



