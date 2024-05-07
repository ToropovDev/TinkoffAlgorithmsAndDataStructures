import heapq

inf = float('inf')


def dijkstra(start, _n, _graph):
    dist = [inf] * (_n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, _u = heapq.heappop(pq)
        if current_dist > dist[_u]:
            continue
        for _v, weight in _graph[_u]:
            distance = current_dist + weight
            if distance < dist[_v]:
                dist[_v] = distance
                heapq.heappush(pq, (distance, _v))
    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

a, b, c = map(int, input().split())

distance_a = dijkstra(a, n, graph)
distance_b = dijkstra(b, n, graph)
distance_c = dijkstra(c, n, graph)

min_path_len = inf
min_path_len = min(min_path_len, distance_a[b] + distance_b[c])
min_path_len = min(min_path_len, distance_a[c] + distance_c[b])
min_path_len = min(min_path_len, distance_b[a] + distance_a[c])
min_path_len = min(min_path_len, distance_b[c] + distance_c[a])
min_path_len = min(min_path_len, distance_c[a] + distance_a[b])
min_path_len = min(min_path_len, distance_c[b] + distance_b[a])

if min_path_len == inf:
    print(-1)
else:
    print(min_path_len)

