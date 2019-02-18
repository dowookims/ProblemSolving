def isPal(text):
    while True:
        if len(text) == 1:
            return True
        if text[0] == text[len(text) - 1]:
            if len(text) == 2:
                return True
            else:
                text = text[1:len(text) - 1]
        else:
            return False


T = int(input())
for TC in range(1, T + 1):
    N, M = list(map(int, input().split()))
    input_case = [0] * N
    for i in range(N):
        input_case[i] = ''.join(input().split())

    for i in range(N):
        for j in range(N - M + 1):
            text = ''
            for k in range(j, j + M):
                text += input_case[i][k]
        if isPal(text):
            break

        for q in range(N - M + 1):
            text = ''
            for w in range(q, q + M):
                text += input_case[w][i]
        if isPal(text):
            break

    print(f'#{TC} {text}')

