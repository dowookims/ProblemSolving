# def getPi(p):
#     p_l = len(p)
#     pi = [0]*p_l
#     j = 0
#     for i in range(1, p_l):
#         while(j > 0 and p[i] != p[j]):
#             j = pi[j-1]
#         if(p[i] == p[j]):
#             pi[i] += j
#     return pi

# def kmp(s, p):
#     ans = []
#     pi = getPi(p)
#     n = len(s)
#     m = len(p)
#     j = 0
#     for i in range(n):
#         while j>0 and s[i] != p[j]:
#             j = pi[j-1]
#         if(s[i] == p[j]):
#             if(j==m-1):
#                 ans.append(i-m+1)
#                 j = pi[j]
#             else:
#                 j += 1
    
#     return ans

T = int(input())
for i in range(1, T+1):
    patterns, texts = list(input().split())
    

