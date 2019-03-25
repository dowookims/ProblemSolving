for TC in range(1, int(input())+1):
    n = float(input())
    r = ''
    while True:
        if len(r)>=13:
            r = 'overflow'
            break
        n *= 2
        if n > 1:
            r += '1'
            n -=1
        elif n==1:
            r += '1'
            break
        else:
            r += '0'
    print("#{} {}".format(TC, r))

'''
     0.625
*2   1.25    1
*2   0.5     0
*2   1       1
'''