'''
쉬운 계단 수
'''
N = int(input())
dp = [[ _ for _ in range(12)] for _ in range(102)]
mod = 1000000000
ans = 0
dp[0] = [0]*10
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, N+1):
    for n in range(10):
        if n == 0:
            dp[i][n] = dp[i-1][1]
        elif n == 9:
            dp[i][n] = dp[i-1][8]
        else:
            dp[i][n] = int((dp[i-1][n-1] +dp[i-1][n+1])%mod)

for n in range(10):
    ans += dp[N][n]

print(int(ans % mod))
