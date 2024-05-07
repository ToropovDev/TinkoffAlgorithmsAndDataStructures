import math

length, num_segments = map(int, input().split())
segment_points = []
points = list(map(int, input().split()))
points.insert(0, 0)
points.append(length)
num_segments += 2

dp = []
for _ in range(num_segments):
    dp.append([0] * num_segments)

for j in range(1, num_segments):
    for i in range(j - 2, -1, -1):
        dp[i][j] = math.inf
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        dp[i][j] += points[j] - points[i]

print(dp[0][num_segments - 1])
