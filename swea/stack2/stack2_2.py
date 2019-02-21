import sys
sys.stdin = open("sample_input2.txt", 'r')
def dfs(case, s):


for TC in range(1, int(input())+1):
    r = int(input())
    s = []
    e = []
    visited=[]
    case = [[] for _ in range(r)]
    for i in range(r):
        case[i] = list(map(int,''.join(input())))
    for i in range(r):
        for j in range(r):
            if s and e:
                break
            elif case[i][j] == 3:
                s = [i,j]
            elif case[i][j] == 2:
                e = [i,j]

    for i in case:
        print(i)
    print(f"s : {r} // e : {r}")
    print('############')
