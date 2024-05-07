# C-LCA

def build_tree(n, parents):
    tree = [[] for _ in range(n)]
    for i, p in enumerate(parents):
        tree[p].append(i + 1)
    return tree


def build_ancestors_and_depth(tree, n, root):
    log_n = 20
    ancestors = [[-1] * log_n for _ in range(n + 1)]
    depths = [0] * (n + 1)

    def dfs(node, par, d):
        ancestors[node][0] = par
        depths[node] = d
        for child in tree[node]:
            dfs(child, node, d + 1)

    dfs(root, -1, 0)

    for i in range(1, log_n):
        for node in range(1, n + 1):
            if ancestors[node][i - 1] != -1:
                ancestors[node][i] = ancestors[ancestors[node][i - 1]][i - 1]

    return ancestors, depths


def lca_query(u, v, ancestors, depths):
    log_n = 20
    if depths[u] < depths[v]:
        u, v = v, u

    for i in range(log_n - 1, -1, -1):
        if depths[u] - (1 << i) >= depths[v]:
            u = ancestors[u][i]

    if u == v:
        return u

    for i in range(log_n - 1, -1, -1):
        if ancestors[u][i] != ancestors[v][i]:
            u = ancestors[u][i]
            v = ancestors[v][i]

    return ancestors[u][0]


n = int(input())
parents = list(map(int, input().split()))
m = int(input())
queries = [tuple(map(int, input().split())) for _ in range(m)]

tree = build_tree(n, parents)
ancestors, depths = build_ancestors_and_depth(tree, n, 0)

for u, v in queries:
    lca = lca_query(u, v, ancestors, depths)
    print(lca)
