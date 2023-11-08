t = int(input())
dp = []

for i in range(3):
    dp.append(1)
dp.append(2)
for i in range(t):
    n = int(input())
    for j in range(4, n):
        dp.insert(j, dp[j - 2] + dp[j - 3])
    print(dp[n - 1])
