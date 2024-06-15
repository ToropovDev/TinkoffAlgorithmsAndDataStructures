# Есть ли цикл?


class Peak:
    def __init__(self, color=0):
        self.color = color


class Graph:
    def __init__(self, connect_list):
        self.connect_list = connect_list
        self.peaks = [Peak() for _ in range(len(connect_list))]
        self.path = []
        self.pathSize = 0


def DFS(peak, graph, cycle_end, cycle_start):
    graph.peaks[peak].color = 1
    for i in graph.connect_list[peak]:
        if graph.peaks[i].color == 0:
            graph.path.append(i)
            graph.pathSize += 1
            if DFS(i, graph, cycle_end, cycle_start):
                return True
        elif graph.peaks[i].color == 1:
            cycle_start[0] = i
            cycle_end[0] = peak
            return True
    graph.peaks[peak].color = 2
    graph.pathSize -= 1
    return False


n, m = map(int, input().split())

connect_list = [[] for _ in range(n)]

for _ in range(m):
    peak1, peak2 = map(int, input().split())
    peak1 -= 1
    peak2 -= 1
    connect_list[peak1].append(peak2)

graph = Graph(connect_list)
has_cycle = 0
cycle_end = [0]
cycle_start = [0]

for i in range(n):
    if graph.peaks[i].color == 0:
        graph.path.append(i)
        graph.pathSize += 1
        if DFS(i, graph, cycle_end, cycle_start):
            has_cycle = 1
            break

print(has_cycle)
