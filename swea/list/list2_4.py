TC = int(input())
for case_num in range(1,TC+1):

    l_c = int(input())

    case = list(map(int, input().split()))

    for i in range(len(case) - 1):
        m_n = i
        for j in range(i + 1, len(case)):
            if case[j] < case[m_n]:
                m_n = j
        case[i], case[m_n] = case[m_n], case[i]

    io= 0
    ie = -1
    c = [0]*l_c
    for i in range(len(case)):
        if i%2 == 0:
            io -= 1
            idx = io
        else:
            ie += 1
            idx = ie
        c[i] = case[idx]
    res = ' '.join(list(map(str, c[0:10])))
    print(f"#{case_num} {res}")