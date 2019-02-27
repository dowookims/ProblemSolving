import sys
sys.stdin= open("1222.txt", "r")

for TC in range(1, 11):
    r = int(input())
    case = input()
    num = [0]*r
    stack = [0]*3
    top = -1
    i = 0
    j = 0
    sum = 0
    for i in range(r):
        if case[i].isdigit():
            sum += int(case[i])
    print(f"#{TC} {sum}")