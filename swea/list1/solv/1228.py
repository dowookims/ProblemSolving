#  1228. [S/W 문제해결 기본] 8일차 - 암호문1
import sys
sys.stdin = open("1228.txt", "r")

for TC in range(1, 11):
    RCN = int(input())
    RCS = input().split()
    CMDN = int(input())
    commands = input().split()
    i = 0
    while i<len(commands):
        if commands[i] == 'I':
            I = int(commands[i+1]) #1
            s = i+3 # 3
            e = i+3 + int(commands[i+2]) # 3 + 5 = 8 || 3 4 5 6 7
            for j in range(s,e):
                RCS.insert(I, commands[j])
                I +=1
            i = e-1
        i += 1
    print(f"#{TC}", end=" ")
    for j in range(10):
        print(RCS[j], end=" ")
    print()

