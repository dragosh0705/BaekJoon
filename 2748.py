n = int(input())
dp = [n]
dp.insert(0, 0)
dp.insert(1, 1)
dp.insert(2, 1)
if n >= 3:
    for i in range(3, n + 1):
        dp.insert(i, dp[i - 1] + dp[i - 2])
print(dp[n])