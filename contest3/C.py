# C-LCA


from collections import deque


def build(graph, depth, dp, max_i, root):
    stack = [(root, 0, 0)]

    while stack:
        vertex, parent, current_depth = stack.pop()
        depth[vertex] = current_depth
        dp[vertex][0] = parent

        for i in range(1, max_i + 1):
            dp[vertex][i] = dp[dp[vertex][i - 1]][i - 1]

        for child in graph[vertex]:
            stack.append((child, vertex, current_depth + 1))


def lca(depth, dp, max_i, u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    diff = depth[u] - depth[v]

    for i in range(max_i + 1):
        if (diff >> i) & 1:
            u = dp[u][i]

    if u == v:
        return u

    for i in range(max_i, -1, -1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]

    return dp[u][0]


n = int(input())
graph = list(map(int, input().split()))

depth = [0] * n
max_i = 1
while (1 << max_i) <= n:
    max_i += 1
dp = [[0] * (max_i + 1) for _ in range(n)]

build(graph, depth, dp, max_i, 0)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(lca(depth, dp, max_i, u - 1, v - 1) + 1)

