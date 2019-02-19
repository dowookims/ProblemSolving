import sys
sys.stdin = open("sample_input.txt", "r")

for TC in range(1, int(input())+1):
    case = input().split()
    top = -1

    d = [0]*len(case)

    for i in range(len(case)):
        if case[i].isdigit():
            top += 1
            d[top] = int(case[i])

        elif case[i] == '.':
            if top:
                print(f"#{TC} error")
                break
            else:
                print(f"#{TC} {d[top]}")


        elif top>=1 and type(d[top-1]) == type(d[top]):
            if case[i] == '+':
                d[top-1] = d[top-1] + d[top]
                d[top]='a'
                top -= 1

            elif case[i] == '-':
                d[top-1] = d[top-1] - d[top]
                d[top] = 'a'
                top -= 1

            elif case[i] == '*':
                d[top-1] = d[top-1] * d[top]
                d[top] = 'a'
                top -= 1

            elif case[i] == '/':
                d[top - 1] = int(d[top - 1] // d[top])
                d[top] = 'a'
                top -= 1
        else:
            print(f"#{TC} error")
            break