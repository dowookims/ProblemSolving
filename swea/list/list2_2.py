TC = int(input())
A = [i for i in range(1,13)]
for case_num in range(1, TC+1):
    N, K = list(map(int, input().split()))
    n = len(A)
    c = []
    for i in range(1<<n):
        cnt_j = []
        for j in range(n+1):
            if i & (1<<j):
                cnt_j.append(A[j])
        if len(cnt_j) == N and sum(cnt_j) == K:
            c.append(cnt_j)
    
    print(f"#{case_num} {len(c)}")