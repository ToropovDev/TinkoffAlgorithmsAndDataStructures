import heapq

max_n = 10 ** 5
graph = [[] for _ in range(max_n)]


def dijkstra(source):
    PQ = []
    distances = [1e9 for _ in range(n + 2)]
    heapq.heappush(PQ, [0, source])
    distances[source] = 0
    while PQ:
        cur_dist, cur = heapq.heappop(PQ)
        if cur_dist > distances[cur]:
            continue
        for v, weight in graph[cur]:
            if distances[v] > distances[cur] + weight:
                distances[v] = distances[cur] + weight
                heapq.heappush(PQ, [distances[v], v])

    return 1 + distances[0]


def get_result(n):
    for j in range(1, n + 1):
        f = j % n
        to = (j + 1) % n
        w = 1
        graph[f].append([to, w])

    for j in range(1, n + 1):
        f = j % n
        to = (10 * j) % n
        w = 0
        graph[f].append([to, w])

    return dijkstra(1)


n = int(input())
print(get_result(n))

