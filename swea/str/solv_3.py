T = int(input())
for TC in range(1, T+1):
    pattern = input().split()
    sentence = input()
    result = 0
    dupl = False
    p = ''
    for i in range(len(pattern)):
        j = 0
        while True:
            if j == len(p):
                break

            if p[j] == pattern[i]:
                dupl = True
                break
            else:
                j+= 1
        if not dupl:
            p += pattern[i]
    
    count_list = [0]*len(p)

    for n in range(len(sentence)):
        for l in range(len(p)):
            if sentence[n] == p[l]:
                count_list[l]+= 1
                break
    result = 0
    for q in range(len(count_list)):
        if result < count_list[q]:
            result = count_list[q]

    print(f"#{TC} {result}")