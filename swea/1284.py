# 1284. 수도 요금 경쟁
import sys
sys.stdin = open("1284.txt","r")

for TC in range(1, int(input())+1):
    P, Q, R, S, W = map(int,input().split())
    B = Q+S*(W-R) if W > R else Q
    print(f"#{TC} {min(W*P, B)}")