# LCA
from math import log2


def build_sparse_table(n, parents):
    log_n = int(log2(n)) + 1
    sparse_table = [[-1] * log_n for _ in range(n)]

    for i in range(n):
        sparse_table[i][0] = parents[i - 1]

    for j in range(1, log_n):
        for i in range(n):
            if sparse_table[i][j - 1] != -1:
                sparse_table[i][j] = sparse_table[sparse_table[i][j - 1]][j - 1]

    return sparse_table


def lca(u, v, depth, sparse_table):
    if depth[u] < depth[v]:
        u, v = v, u

    log_n = len(sparse_table[0])
    for i in range(log_n - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = sparse_table[u][i]

    if u == v:
        return u

    for i in range(log_n - 1, -1, -1):
        if sparse_table[u][i] != -1 and sparse_table[u][i] != sparse_table[v][i]:
            u = sparse_table[u][i]
            v = sparse_table[v][i]

    return sparse_table[u][0]


n = int(input())
parents = list(map(int, input().split()))
m = int(input())

sparse_table = build_sparse_table(n, parents)

depth = [0] * n
for i in range(1, n):
    depth[i] = depth[parents[i - 1]] + 1

result = []

for _ in range(m):
    u, v = map(int, input().split())
    result.append(lca(u, v, depth, sparse_table))

for res in result:
    print(res)
