# Топологическая сортировка


def is_top_sort(n, connect_list, perm):
    peak_degrees = [0] * (n + 1)

    for u in range(1, n + 1):
        for v in connect_list[u]:
            peak_degrees[v] += 1

    for i in range(n):
        if peak_degrees[perm[i]] != 0:
            return "NO"
        for v in connect_list[perm[i]]:
            peak_degrees[v] -= 1

    return "YES"


n, m = map(int, input().split())
connect_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    connect_list[u].append(v)

perm = list(map(int, input().split()))

print(is_top_sort(n, connect_list, perm))
