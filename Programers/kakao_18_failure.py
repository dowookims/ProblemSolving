'''
(2018년)KAKAO BLIND RECRUITMENT
실패율
'''
N = 4
stages = [4, 4, 4, 4, 4]
players = [0] * (N+2)
users = [0]*(N+2)
fails = [0]*(N+2)
v = [0]*(N+2)
res = [0]*N
gn = len(stages)
for i in range(len(stages)):
    users[stages[i]] += 1

for i in range(1, N+2):
    if i == 1:
        players[i] = gn

    else:
        players[i] = gn - users[i-1]
        gn = players[i]
    if players[i] == 0:
        continue
    else:
        fails[i] = users[i] / players[i]

for i in range(1, N+1):
    if v[i]:
        mv = 0
        mi = i
    else:
        mv = fails[i]
        mi = i
    for j in range(1, N+1):
        if j == i:
            continue
        if fails[j] > mv and not v[j]:
            mi = j
            mv = fails[j]
        elif fails[j] == mv and not v[j]:
            if j < mi:
                mi = j
    v[mi] = 1
    res[i-1] = mi

print(res)