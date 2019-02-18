# 1936. 1:1 가위바위보
#
# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
#
# 입력
# 가위 1 바위 2 보 3
# 입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.
# 출력
# A가 이기면 A, B가 이기면 B를 출력한다.

a,b = map(int,input().split())

if a == 1:
    c = 'B' if a-b == -1 else 'A'
elif a == 2:
    c= 'B' if a-b == -1 else 'A'
else:
    c= 'B' if a-b == 2 else 'A'
print(c)


