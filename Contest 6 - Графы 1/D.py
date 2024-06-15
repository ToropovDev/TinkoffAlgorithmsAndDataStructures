# Один голодный конь
from collections import deque


class Peak:
    def __init__(self, color=0, data=0, coords=(0, 0)):
        self.color = color
        self.data = data
        self.coords = coords
        self.path = (0, 0)
        self.depth = 0
        self.path_n = 0


class Graph:
    def __init__(self, connect_list, size):
        self.connect_list = connect_list
        self.peaks = [Peak(0, i * size + j, (i, j)) for i in range(size) for j in range(size)]


def BFS(graph, start):
    q = deque()
    graph.peaks[start].color = 1
    q.append(graph.peaks[start])
    while q:
        peak = q.popleft()
        peak_data = peak.elements
        for i in graph.connect_list[peak_data]:
            if graph.peaks[i].color == 0:
                graph.peaks[i].color = 1
                graph.peaks[i].path = (graph.peaks[peak_data].coords[0], graph.peaks[peak_data].coords[1])
                graph.peaks[i].path_n = peak_data
                graph.peaks[i].depth = graph.peaks[peak_data].depth + 1
                q.append(graph.peaks[i])
        graph.peaks[peak_data].color = 2


n = int(input())

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x1 -= 1
x2 -= 1
y1 -= 1
y2 -= 1

connect_list = [[] for _ in range(n * n)]

for i in range(n):
    for j in range(n):
        if n > i + 2 >= 0:
            if n > j + 1 >= 0:
                connect_list[i * n + j].append((i + 2) * n + j + 1)
            if n > j - 1 >= 0:
                connect_list[i * n + j].append((i + 2) * n + j - 1)
        if n > i - 2 >= 0:
            if n > j + 1 >= 0:
                connect_list[i * n + j].append((i - 2) * n + j + 1)
            if n > j - 1 >= 0:
                connect_list[i * n + j].append((i - 2) * n + j - 1)
        if n > j + 2 >= 0:
            if n > i + 1 >= 0:
                connect_list[i * n + j].append((i + 1) * n + j + 2)
            if n > i - 1 >= 0:
                connect_list[i * n + j].append((i - 1) * n + j + 2)
        if n > j - 2 >= 0:
            if n > i + 1 >= 0:
                connect_list[i * n + j].append((i + 1) * n + j - 2)
            if n > i - 1 >= 0:
                connect_list[i * n + j].append((i - 1) * n + j - 2)

graph = Graph(connect_list, n)
start = x1 * n + y1
finish = x2 * n + y2

BFS(graph, start)

if graph.peaks[finish].depth != 0:
    print(graph.peaks[finish].depth)
    p = []
    v = graph.peaks[finish].coords
    while v != graph.peaks[start].coords:
        p.append(v)
        v = graph.peaks[v[0] * n + v[1]].path
    p.append(v)
    for coords in reversed(p):
        print(coords[0] + 1, coords[1] + 1)
elif start == finish:
    print(0)
    print(x1 + 1, y1 + 1)
else:
    print(-1)
