n, m = map(int, input().split())


class Peak:
    def __init__(self, visited=0):
        self.visited = visited
        self.path = []
        self.count_in_component = 0


class Graph:
    def __init__(self, connect_list):
        self.connect_list = connect_list
        self.peaks = [Peak() for _ in connect_list]


def DFS(start, current, graph: Graph):
    if not graph.peaks[current].visited:
        graph.peaks[start].path.append(current + 1)
        graph.peaks[current].visited = 1
        for i in graph.connect_list[current]:
            if not graph.peaks[i].visited:
                graph.peaks[start].count_in_component += 1
                DFS(start, i, graph)
        graph.peaks[current].visited = 2


connect_list = [[] for _ in range(n)]
for _ in range(m):
    peak1, peak2 = map(int, input().split())

    connect_list[peak1-1].append(peak2-1)
    connect_list[peak2-1].append(peak1-1)

graph = Graph(connect_list)
count = 0

for i in range(n):
    if graph.peaks[i].visited == 0:
        DFS(i, i, graph)
        count += 1

print(count)
for i in range(n):
    path = graph.peaks[i].path
    if path:
        print(len(path))
        print(*sorted(path))
