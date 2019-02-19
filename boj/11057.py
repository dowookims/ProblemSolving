N = int(input())

dp = [[ _ for _ in range(10)] for _ in range(1001)]

dp[0] = [0]*10
dp[1] = [1]*10
ans = 0
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, 10):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

for i in range(0, 10):
    ans += dp[N][i]
print(ans % 10007)