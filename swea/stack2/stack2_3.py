import sys
sys.stdin = open("sample_input3.txt", "r")

def div_list(case):
    if len(case[0])== 1 or len(case[0])==2:
        return
    return div_list([[case[0:idx], case[idx+1:len(case)]]])

for TC in range(1, int(input())+1):
    N = int(input())
    t = 0
    while True:
        t +=1
        if N == 1:
            break
        else:
            N = N//2

    case = list(map(int, input().split()))
    idx = len(case) // 2
    a = [case[0:idx],case[idx+1:len(case)]]
    print(div_list(a))

