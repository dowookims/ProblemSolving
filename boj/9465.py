'''
스티커
스티커 2n개 구매, 2행 n열
xxxxx
xxxxx
뗀 스티커의 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없음
각 테스트 케이스 마다, 2n개의 스티커 중에서 두 변을 공유하지 않는 스티커 점수의 최댓값을 출력한다.
'''
T = int(input())
for TC in range(1, T+1):
    n = int(input())
    s_l = []
    d =[[i for i in range(n)] for _ in range(3)]
    for _ in range(2):
        s_l.append(list(map(int, input().split())))
    d[0][0] = 0
    d[1][0] = s_l[0][0]
    d[2][0] = s_l[1][0]
    for i in range(1,n):
        d[0][i] = max(d[0][i-1], d[1][i-1], d[2][i-1])
        d[1][i] = max(d[0][i-1], d[2][i-1], d[0][i-1])
        d[2][i] = max(d[0][i - 1], d[1][i - 1], d[2][i - 1])
    print(max(d[0][n - 1], d[1][n - 1], d[2][n - 1]))
