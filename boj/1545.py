# 1545. 거꾸로 출력해 보아요
#
# 주어진 숫자만큼 # 을 출력
# 입력 8
# 
# 출력 8 7 6 5 4 3 2 1 0

a = int(input())
for i in range(a,0,-1):
    print(i, end=' ')
    if i==1: print('0', end='')
