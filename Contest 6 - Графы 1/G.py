# Offline-семинар

inf = float('inf')


def floyd_warshall(n, graph):
    distances = [[inf] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for u, v, w in graph:
        distances[u - 1][v - 1] = w
        distances[v - 1][u - 1] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


def find_center(distances):
    max_distance = [max(row) for row in distances]
    min_max_distance = min(max_distance)
    return max_distance.index(min_max_distance) + 1


n, m = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(m)]

distance = floyd_warshall(n, graph)
center = find_center(distance)

print(center)
