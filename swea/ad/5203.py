'''
babygin
'''

import sys
sys.stdin = open("5203.txt", "r")


for TC in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    a = [0]*10
    b = [0]*10
    res = 0
    for i in range(12):
        b1, b2, f1, f2 = cards[i] - 1, cards[i] - 2, cards[i] + 1, cards[i] + 2
        if f1 == 10:
            f1 = 0
            f2 = 1
        elif f1 == 9:
            f2 = 0
        if b1 == -1:
            b1 = 9
            b2 = 8
        elif b1 == 0:
            b2 = 9

        if i % 2 == 0:
            a[cards[i]] += 1
            if a[cards[i]] == 3:
                res = 1
                break
            else:
                if a[cards[i]] and a[b1] and a[b2]:
                    res = 1
                    break
                elif a[cards[i]] and a[f1] and a[f2]:
                    res = 1
                    break
                elif a[b1] and a[cards[i]] and a[f1]:
                    res = 1
                    break

        else:
            b[cards[i]] += 1
            if b[cards[i]] == 3:
                res = 2
                break
            else:
                if b[cards[i]] and b[b1] and b[b2]:
                    res = 2
                    break
                elif b[cards[i]] and b[f1] and b[f2]:
                    res = 2
                    break
                elif b[b1] and b[cards[i]] and b[f1]:
                    res = 2
                    break

    print('#{} {}'.format(TC, res))