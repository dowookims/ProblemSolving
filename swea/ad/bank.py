for TC in range(1, int(input())+1):
    bin = input()
    binums = 0
    for i in range(0, len(bin)):
        if int(bin[i]):
            binums += 2 **(len(bin)-i-1)
    tre = input()
    trenums = 0
    for i in range(0, len(tre)):
        if int(tre[i]):
            trenums += int(tre[i]) * 3 **(len(tre)-i-1)
    res = 0
    if binums - trenums > 0:
        for i in range(len(bin)):
            if res:
                break
            for j in range(len(tre)):
                if res:
                    break
                for k in range(0,3):
                    if binums - 2 ** i == trenums + k * 3 ** j:
                        res = binums - 2 ** i
                        break
    elif binums == trenums:
        res = binums
    else:
        for i in range(len(bin)):
            if res:
                break
            for j in range(len(tre)):
                if res:
                    break
                for k in range(0,3):
                    if binums + 2 ** i == trenums - k * 3 ** j:
                        res = binums + 2 ** i
                        break

    print("#{} {}".format(TC, res))