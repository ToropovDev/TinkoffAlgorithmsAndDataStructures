import heapq


def dijkstra(_graph, start, max_weight, _n):
    INF = float('inf')
    min_time = [INF] * (_n + 1)
    min_time[start] = 0
    pq = [(0, start)]

    while pq:
        current_time, u = heapq.heappop(pq)

        if current_time > min_time[u]:
            continue

        for v, time, weight in _graph[u]:
            if weight >= max_weight and min_time[v] > min_time[u] + time:
                min_time[v] = min_time[u] + time
                heapq.heappush(pq, (int(min_time[v]), v))

    return min_time[_n]


def check(mugs, _graph, _n, _max_time) -> bool:
    truck_weight = 3000000 + mugs * 100
    return dijkstra(_graph, 1, truck_weight, _n) <= _max_time


def binary_search(_graph, _n, _max_time):
    left, right = 0, 100000000
    best = 0

    while left <= right:
        middle = (left + right) // 2
        if check(middle, _graph, _n, _max_time):
            best = middle
            left = middle + 1
        else:
            right = middle - 1

    return best


n, m = map(int, input().split())
index, max_time = 2, 1440
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, t, w = map(int, input().split())
    graph[u].append([v, t, w])
    graph[v].append([u, t, w])
    index += 4

result = binary_search(graph, n, max_time)
print(result)


