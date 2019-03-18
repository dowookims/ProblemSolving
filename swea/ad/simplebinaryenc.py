#단순 2진 암호 코드
import sys
sys.stdin = open("st.txt.","r")


def getNum(n):
    for i in range(10):
        if n == enc[i]:
            return i
    return False

enc = ['0001101',
       '0011001',
       '0010011',
       '0111101',
       '0100011',
       '0110001',
       '0101111',
       '0111011',
       '0110111',
       '0001011']



for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    res = 0
    s = []
    for i in range(N):
        case = input()
        idx = M-1
        while idx >= 0:
            if case[idx] == '1':
                s.append(getNum(case[idx-6:idx+1]))
                idx -= 7
            else:
                idx -= 1

    if ((s[1]+s[3]+s[5]+s[7])*3+s[0]+s[2]+s[4]+s[6]) % 10:
        res = 0
    else:
        for i in range(8):
            res += s[i]
    print("#{} {}".format(TC, res))
