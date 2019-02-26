import sys
sys.stdin = open("4881.txt", "r")

def cal(s, row, min_num, r, res):
    if row == 10:
        print('yes')
        if min_num < res:
            res = min_num
            return res
        else: 
            return
    for i in range(row, r):
        for j in range(r):
            if calculated[j]:
                pass
            else:
                if row ==0:
                    j = s
                min_num += case[i][j]
                calculated[j] = 1
                row += 1
                cal(s, row, min_num,r, res)

for TC in range(1, int(input())+1):
    r = int(input())
    case = [[] for _ in range(r)]
    for i in range(r):
        case[i] = list(map(int, input().split()))
    res = 987654321
    for i in range(r):
        calculated = [0 for _ in range(r)]
    for i in range(r):
        a =  cal(i, 0, 0, r, res)
        if a < res:
            res = a
            
    


    print(f'{TC} {res}')