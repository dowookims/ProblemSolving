prices = [1, 2, 3, 2, 3]

flag = False
s = 0
e = 0
cnt = 1
answer = [0] * len(prices)

for i in range(len(prices)-1):
    if prices[i] > prices[i+1]:
        if not flag:
            answer[i] = 1
        else:
            cnt += 1
            e = i
            for j in range(s, e):
                answer[j] = cnt
                cnt -= 1
            cnt = 1
            s = 0
            e = 0
            answer[i] = 1
            flag = False
    else:
        if not flag:
            flag = True
            s = i
            if i+1 == len(prices)-1 :
                answer[i] = 1
            cnt += 1
        else:
            cnt += 1

print(answer)