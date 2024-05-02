import heapq


class Graph:
    def __init__(self, n):
        self.connect_list = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.connect_list[u].append([v, w])
        self.connect_list[v].append([u, w])


def dijkstra(graph, start):
    n = len(graph.connect_list)
    distance = [float('inf')] * n
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > distance[node]:
            continue
        for neighbor, weight in graph.connect_list[node]:
            if distance[node] + weight < distance[neighbor]:
                distance[neighbor] = distance[node] + weight
                heapq.heappush(pq, (distance[neighbor], neighbor))

    return distance


def find_shortest_path_through_ABC(graph, a, b, c):
    n = len(graph.connect_list)
    shortest_paths = [dijkstra(graph, i) for i in range(n)]

    min_time = float('inf')
    for u in (a, b, c):
        for v in (a, b, c):
            if u != v:
                for w in (a, b, c):
                    if w != u and w != v:
                        min_time = min(
                            min_time,
                            shortest_paths[u][v] + shortest_paths[v][w]
                        )

    return min_time if min_time < float('inf') else -1


n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph.add_edge(u - 1, v - 1, w)

a, b, c = map(int, input().split())

result = find_shortest_path_through_ABC(graph, a-1, b-1, c-1)
print(result)
