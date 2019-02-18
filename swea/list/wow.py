def getNum(strs):
    if strs =='ZRO': return 0
    elif strs =='ONE': return 1
    elif strs == 'TWO': return 2
    elif strs == 'THR': return 3
    elif strs == 'FOR': return 4
    elif strs == 'FIV': return 5
    elif strs == 'SIX': return 6
    elif strs == 'SVN': return 7
    elif strs == 'EGT': return 8
    else: return 9

T = int(input())
t_l = ["ZRO ","ONE ","TWO ","THR ","FOR ","FIV ","SIX ","SVN ","EGT ","NIN "]

for _ in range(T):
    a, b = input().split()
    f_l = list(input().split())
    s_l = [0]*10

    for word in f_l:
        s_l[getNum(word)] += 1
    print(f"{a}")
    for i in range(len(s_l)):
        print(f"{t_l[i]*s_l[i]}")