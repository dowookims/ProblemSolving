def process_solution(a, k, r):

def c_c(c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, r):
    c = [0]*2
    k = 0
    if k == r:
        process_solution(a,k,r)
    else:
        k += 1
        visited = c_c(c)
        for i in range(visited):
            a[k] = c[i]
            backtrack(a,k,r)


for TC in range(1, int(input())+1):
    r = int(input())
    case = [ [] for _ in range(r)]
    for i in range(r):
        case[i] = list(map(int, input().split()))

    for i in range(r):
        for j in range(r):

    print(f"#{TC} {sum}")