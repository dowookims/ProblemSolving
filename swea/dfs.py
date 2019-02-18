graph = '1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7'
c = list(map(int, graph.split(',')))
# near_list = [[0]*7]] # 이렇게 만들면 참조 문제가 발생하므로 for 문으로 돌려서 만들어야 한다.
near_list = [0]*7
for i in range(7):
    near_list[i] = [0]*7


while True:
    if len(c) == 0:
        break
    x,y = c[0:2]
    near_list[x-1][y-1] = 1
    near_list[y-1][x-1] = 1
    c = c[2:]
print(near_list)
visited = [0]*7

i = 0
q = near_list[i]
print('------')
print(q)
print(type(q))
print('------')
c = True
while c:
    if not visited[i]:
        visited[i] = 1
        j = 0
        while True:
            if near_list[i][j] == 1 and not visited[j]:
                break
            else:
                j += 1
        print(f'{i+1} ', end=" ")
        i = j
    i += 1
    k = 0
    for i in range(7):
        if visited[i]:
            k += 1
        if k==7:
            c = False
            break
'''
# 상태 공간 트리(트리트리트리)
def DFSr(v):
    print(v)
    visited[v] = True

    for i in range(1,8):
        if G[v][i] and not visited[i]:
            DFSr(i)

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4 , 6, 5, 6, 6, 7, 3, 7]
visited = [0]*8
G = [[0]*8 for _ in range(8)]

for i in range(0, len(edges), 2):

'''
    

