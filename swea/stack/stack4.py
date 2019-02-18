T = int(input()) + 1
for TC in range(1, T):
    str = input()
    top = -1
    stack = [0]*len(str)

    for i in range(len(str)):
        if top != -1 and str[i] == stack[top]:
            stack[top] = 0
            top -= 1
        else:
            top += 1
            stack[top] = str[i]

    print(f"#{TC} {top+1}")