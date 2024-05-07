def get_min_cost(n, cost):
    dp = [0] * n
    dp[0] = cost[0]
    for i in range(1, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    return dp[-1]


n = int(input())
s = list(map(int, input().split()))

print(get_min_cost(n, s))
