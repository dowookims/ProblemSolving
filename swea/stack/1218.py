import sys
sys.stdin = open("input8.txt", "r")
for TC in range(1,11):
    r = int(input())
    case = input()
    stack = [0]*r
    top = -1
    b = ['{','(','[','<']
    b_r = ['}', ')',']', '>']
    res = 1
    for i in range(len(case)):
        if case[i] in b:
            top +=1
            stack[top] = case[i]
        else:
            for j in range(4):
                if b_r[j] == case[i]:
                    if b[j] != stack[top]:
                        res = 0
                        break
                    else:
                        stack[top] = ''
                        top -=1
                        break
        if res ==0:
            break
    print(f"#{TC} {res}")
