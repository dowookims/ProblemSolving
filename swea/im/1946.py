# 1946 간단한 압축 풀기
import sys
sys.stdin = open("1946.txt", "r")

for TC in range(1, int(input())+1):
    n = int(input())
    cnt = 1
    print("#{}".format(TC))
    for i in range(n):
        c, l = input().split()
        for i in range(int(l)):
            print(c, end="")
            cnt+= 1
            if cnt>10:
                print()
                cnt = 1
    print()

