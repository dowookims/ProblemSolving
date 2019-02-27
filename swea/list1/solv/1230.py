#  1230. [S/W 문제해결 기본] 8일차 - 암호문3

import sys
sys.stdin = open("1230.py.txt", "r")

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
            e = s + int(commands[i+2]) # 3 + 5 = 8 || 3 4 5 6 7
            for j in range(s,e):
                RCS.insert(I, commands[j])
                I +=1
            i = e-1

        elif commands[i] == 'D':
            I = int(commands[i+1])
            e = int(commands[i+2])
            for _ in range(e):
                RCS.pop(I)
            i += 2
        elif commands[i] == 'A':
            n = int(commands[i+1])
            s = i+2
            e = s + n
            for j in range(s,e):
                commands.append(commands[j])
            i = e -1
        i += 1
    print(f"#{TC}", end=" ")
    for j in range(10):
        print(RCS[j], end=" ")
    print()