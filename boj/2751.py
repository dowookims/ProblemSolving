a = int(input())

num_list = [0]*a
for i in range(a):
    num_list[i] = int(input())
num_list.sort()
for item in num_list:
    print(item)
