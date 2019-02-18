'''
6692. 다솔이의 월급 상자

상자에는 p의 확률로 x만원이 들어 있다.
다솔이가 받을 수 있는 월급의 평균은 얼마인지 구해보자
'''

a = int(input())
for i in range(1, a+1):
    b = int(input())
    q = 0
    for __ in range(b):
        wp, wx = list(map(float, input().split()))
        q += wp*wx
    print(f"#{i} {q}")
