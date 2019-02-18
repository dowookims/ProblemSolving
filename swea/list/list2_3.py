TC = int(input())

# 재귀로 구현
# def binarySearch(min_p, max_p, a, c=0):
#     middle = int((1+max_p)/2)
#     if a == middle:
#         return c
#     elif a>middle:
#         c+=1
#         return binarySearch(middle, max_p, a, c)
#     else:
#         c+=1
#         return binarySearch(1, middle, a, c)
def binaySearch(max_p, a):
    cnt = 0
    min_p = 1
    while(True):
        middle = int((min_p+max_p)/2)
        if a == middle:
            return cnt
        elif a>middle:
            min_p = middle
        else :
            max_p =middle
        cnt += 1
for case_num in range(1, TC+1):
    winner = 0
    T_P, A_P, B_P = list(map(int, input().split()))
    
    c_A_P = binaySearch(T_P, A_P)
    c_B_P = binaySearch(T_P, B_P)
    if c_A_P > c_B_P:
        winner = 'B'
    elif c_A_P == c_B_P:
        winner = 0
    else:
        winner = 'A'
    print(f"#{case_num} {winner}")
