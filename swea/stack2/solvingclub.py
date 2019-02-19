import sys
sys.stdin = open("input2.txt", "r")

def mb(i):
    b_top1 = -1
    b_top2 = -1
    b_stack1 = [0] * n
    b_stack2 = [0] * n
    while case[i] == ')':
        if case[i].isdigit():
            b_top1 += 1
            b_stack1[b_top1] = int(case[i])
        elif case[i] =='(':
            b_stack1 + mb(i)
        elif case[i] =='*':
            if b_stack2[b_top2] == '+':
                b_top2+= 1
                b_stack2[b_top2] = '+'
                b_stack2[b_top2-1] = '*'
            else:
                b_top2 += 1
                b_stack2[b_top2] = case[i]
        else:
            b_top2 += 1
            b_stack2[b_top2] = case[i]
        print('#############')
        print(case[i])
        print('#############')
        i += 1
    return b_stack1 + b_stack2


for TC in range(1, 11):
    n = int(input())
    stack = [0]*n
    top = -1
    case = list(''.join(input()))
    print(case)
    c = mb(0)
    print(c)