# Кратчайший путь
import heapq


def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True

        for neighbor, weight in graph[node]:
            if not visited[neighbor] and distances[neighbor] > dist + weight:
                distances[neighbor] = dist + weight
                heapq.heappush(pq, (dist + weight, neighbor))

    return distances


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start - 1].append((end - 1, weight))
    graph[end - 1].append((start - 1, weight))  # для неориентированного графа добавляем обратное ребро

distances = dijkstra(graph, 0)

print(*distances)


