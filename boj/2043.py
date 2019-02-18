# 2043. 서랍의 비밀번호
#
# P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
# P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.
#
# 입력
# 123 100
# 출력
# 24
# import sys

# sys.stdin => 입출력에서 이거 씀(빠르다)

a,b = [int(x) for x in input().split()]
a,b = map(int,input().split())
print(a-b+1)