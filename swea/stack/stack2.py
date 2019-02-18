TC = int(input())
for T in range(1, TC+1):
    str = input()
    top = -1
    stack = [0]*len(str)
    res = 0
    for item in str:
        if item =='{' or item=='(':
            top += 1
            stack[top] = item
        elif item =='}' or item==')':
            if top == -1:
                stack[0] = 1
                break
            elif (stack[top] == '{' and item ==')') or (stack[top] == '(' and item =='}'):
                break
            else:
                stack[top] = 0
                top -= 1

    if top == -1 and stack[0] == 0:
        res = 1
    print(f"#{T} {res}")