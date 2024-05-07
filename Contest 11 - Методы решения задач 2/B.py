from math import log2


def build_sparse_table(n, parents):
    log_n = int(log2(n)) + 1
    sparse_table = [[-1] * log_n for _ in range(n)]

    for i in range(n):
        sparse_table[i][0] = parents[i-1]

    for j in range(1, log_n):
        for i in range(n):
            if sparse_table[i][j-1] != -1:
                sparse_table[i][j] = sparse_table[sparse_table[i][j-1]][j-1]

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


def find_min_cost_path(n, edges, queries):
    adj_list = [[] for _ in range(n)]
    for i in range(1, n):
        parent, cost = edges[i-1]
        adj_list[i].append((parent, cost))
        adj_list[parent].append((i, cost))

    depth = [0] * n
    stack = [(0, -1, 0)]
    while stack:
        node, parent, d = stack.pop()
        depth[node] = d
        for neighbor, _ in adj_list[node]:
            if neighbor != parent:
                stack.append((neighbor, node, d + 1))

    sparse_table = build_sparse_table(n, [edge[0] for edge in edges])

    results = []
    for query in queries:
        u, v = query
        lca_node = lca(u, v, depth, sparse_table)

        min_cost = float('inf')
        current = u
        while current != lca_node:
            for neighbor, cost in adj_list[current]:
                if neighbor == sparse_table[current][0]:
                    min_cost = min(min_cost, cost)
                    current = neighbor
                    break

        current = v
        while current != lca_node:
            for neighbor, cost in adj_list[current]:
                if neighbor == sparse_table[current][0]:
                    min_cost = min(min_cost, cost)
                    current = neighbor
                    break

        results.append(min_cost)

    return results


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

result = find_min_cost_path(n, edges, queries)
for res in result:
    print(res)
