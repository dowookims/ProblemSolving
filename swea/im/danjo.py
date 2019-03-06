import sys
sys.stdin = open("danjo.txt", "r")


def danjo(n):
    flag = True
    nlen = len(str(n))-1
    while nlen>0:
        bef = n//(10**nlen)
        aft = (n%(10**nlen))//10**(nlen-1)
        if bef > aft:
            flag = False
            break
        n = n%(10**nlen)
        nlen -= 1
    return flag

for TC in range(1, int(input())+1):
    n = int(input())
    case = list(map(int, input().split()))
    danjo_list = []
    for i in range(n-1):
        for j in range(i+1, n):
            num = case[i]*case[j]

            if danjo(num):
                danjo_list.append(num)
    if danjo_list:
        print("#{} {}".format(TC, max(danjo_list)))
    else:
        print("#{} -1".format(TC))



