
for TC in range(1, int(input())+1):
    bin = input()
    tre = input()
    binary = int(bin, 2)
    trimal = int(tre, 3)
    res = 0
    res2 = []
    for i in range(len(bin)):
        if int(bin[i]) and i:
            res2.append(binary - 2 ** (len(bin)-i-1))
        else:
            res2.append(binary + 2 ** (len(bin)-i-1))

    for j in range(len(tre)):
        if int(tre[j]) == 0:
            if trimal + 3**(len(tre)-j-1) in res2:
                res = trimal+3**(len(tre)-j-1)
                break
            elif trimal + 2*(3**(len(tre)-j-1)) in res2:
                res = trimal+2*(3**(len(tre)-j-1))
                break
        elif int(tre[j]) == 1:
            if trimal + (3 ** (len(tre) - j - 1)) in res2:
                res = trimal + (3 ** (len(tre) - j - 1))
                break
            elif trimal-3**(len(tre)-j-1) in res2:
                res = trimal-3**(len(tre)-j-1)
                break
        else:
            if trimal - 3 ** (len(tre) - j - 1) in res2:
                res = trimal - 3 ** (len(tre) - j - 1)
                break
            elif trimal - 2*(3 ** (len(tre) - j - 1)) in res2:
                res = trimal - 2*(3 ** (len(tre) - j - 1))
                break
    print("#{} {}".format(TC, res))