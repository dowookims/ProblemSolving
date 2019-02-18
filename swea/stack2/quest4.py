def process_solution(a,k):
    sum = 0
    for i in range(1, 11):
        if a[i] == True:
            sum += i
    if sum == 10:
        for i in range(1,11):
            if a[i] == True:
                print(i, end =' ')
        print()


def construct_candidates(a,k, input,c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    global cnt
    cnt += 1
    c = [0]*100

    if k == input:
        process_solution(a,k)
    else:
        k += 1
        ncandidates = construct_candidates(a,k,input,c) #True or False
        for i in range(ncandidates): #2번돈다
            a[k] = c[i] # 깊이에 들어가면 True 또는 False를 반환 끝까지 가면 10까지 가고 반환
            backtrack(a,k,input)

# a []
a = [0] * 11
cnt = 0
backtrack(a, 0, 10)
print(cnt)
    