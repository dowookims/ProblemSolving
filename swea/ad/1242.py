import sys
sys.stdin = open("1242.txt", "r")

nums = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

crypto = {
    '3211':'0', '2221': '1', '2122':'2', '1411' : '3', '1132' : '4',
    '1231' : '5', '1114' : '6', '1312' : '7', '1213':'8', '3112':'9'
}

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    cases = []
    cl = [0 for _ in range(2000)]
    res = 0
    cryptoList = []
    for _ in range(N):
        case = []
        if not cases:
            cases.append(input())
        else:
            case = input()
            if case in cases:
                continue
            else:
                cases.append(case)

        for i in range(len(case)):
            a = nums[case[i]]
            cl[i*4], cl[i*4+1], cl[i*4+2], cl[i*4+3] = a[0], a[1], a[2], a[3]
        r = 1999
        cnt = 0

        while r >= 0:
            d = [0, 0, 0, 0]
            if int(cl[r]):
                while int(cl[r]):
                    d[3] += 1
                    r -= 1
                while not int(cl[r]):
                    d[2] += 1
                    r -= 1
                while int(cl[r]):
                    d[1] += 1
                    r -= 1
                while not int(cl[r]):
                    d[0] += 1
                    r -= 1
                    if cnt:
                        if (sum(d) // cnt) == 7:
                            break
                cnt = sum(d) // 7
                c = ''
                for i in range(4):
                    c += str(d[i]//cnt)

                cryptoList.append(int(crypto[c]))
            else:
                cnt = 0
                r -= 1
    d = []
    for i in range(0, len(cryptoList), 8):
        if (cryptoList[(i+2)]+cryptoList[(i+4)]+cryptoList[(i+6)] + (cryptoList[(i+1)] + cryptoList[(i+3)] + cryptoList[(i+5)] + cryptoList[(i+7)]) * 3 + cryptoList[i]) % 10 == 0:
            if not d:
                d.append(cryptoList[i:i+8])
                res += sum(cryptoList[i:i+8])
            else:
                if cryptoList[i:i+8] in d:
                    pass
                else:
                    d.append(cryptoList[i:i + 8])
                    res += sum(cryptoList[i:i + 8])
    print("#{} {}".format(TC, res))