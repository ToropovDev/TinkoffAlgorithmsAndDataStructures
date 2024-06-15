# Система непересекающихся множеств


class dsuNode:
    def __init__(self, v):
        self.parent = v
        self.rank = 0
        self.min_elem = v
        self.max_elem = v
        self.count_elem = 1


def dsu_get(dsu, v):
    if v == dsu[v].parent:
        return v
    dsu[v].parent = dsu_get(dsu, dsu[v].parent)
    return dsu[v].parent


def dsu_union(dsu, x, y):
    x = dsu_get(dsu, x)
    y = dsu_get(dsu, y)
    if x != y:
        if dsu[x].rank < dsu[y].rank:
            x, y = y, x
        if dsu[x].rank == dsu[y].rank:
            dsu[x].rank += 1
        dsu[y].parent = x
        dsu[x].min_elem = min(dsu[x].min_elem, dsu[y].min_elem)
        dsu[x].max_elem = max(dsu[x].max_elem, dsu[y].max_elem)
        dsu[x].count_elem += dsu[y].count_elem


n, m = map(int, input().split())
dsu = [dsuNode(i) for i in range(n)]

result_list = []

for _ in range(m):
    line = input().split()
    operation_type = line[0]
    if operation_type == "union":
        x, y = map(int, line[1:])
        dsu_union(dsu, x - 1, y - 1)
    else:
        x = int(line[1])
        result1 = dsu[dsu_get(dsu, x - 1)]
        result_list.append([result1.min_elem + 1, result1.max_elem + 1, result1.count_elem])

for res in result_list:
    print(*res)
