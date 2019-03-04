def preorder_traverse(T):
    print(T+1, end=" ")
    child = []
    for i in range(len(matrix[T])):
        if matrix[T][i]:
            child.append(i)

    for item in child:
        preorder_traverse(item)
'''
def preorder_traverse(T):
    if T:
        print("%d" % T, end =" ")
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

n = int(input())
tree = [[0] * 2 for _ in range(n+1)]

templ = list(map(int, input().split()))

for i in range(len(templ)// 2):
    parent, child = templ[i * 2], templ[i * 2 + 1]
    if not tree[parent][0] :
        tree[parent][0] = child
    else:
    tree[parent][1] = child

preorder_traverse(1)
print()
'''

V = 13
E = 12
a = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
matrix = [[0 for _ in range(13)] for _ in range(13) ]
for i in range(0,len(a), 2):
    matrix[a[i]-1][a[i+1]-1] = 1

preorder_traverse(0)