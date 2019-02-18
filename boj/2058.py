# 2058. 자릿수 더하기
#
# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
# 자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)
# 입력
# 자연수 N
# 출력
# 각 자릿수의 합을 출력한다.

a = int(input())
b=[]
while True:
    if a<10:
        b.append(a)
        break
    b.append(a%10)
    a= a//10
print(sum(b))