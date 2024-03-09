import random

MAXN = 1000  # замените на максимальное число вершин в графе

g = [[] for _ in range(MAXN)]  # граф
q = [[] for _ in range(MAXN)]  # все запросы
dsu = list(range(MAXN))
ancestor = list(range(MAXN))
u = [False] * MAXN

def dsu_get(v):
    return v if v == dsu[v] else dsu_get(dsu[v])

def dsu_unite(a, b, new_ancestor):
    a, b = dsu_get(a), dsu_get(b)
    if random.getrandbits(1):
        a, b = b, a
    dsu[a] = b
    ancestor[b] = new_ancestor

def dfs(v):
    dsu[v] = v
    ancestor[v] = v
    u[v] = True
    for i in range(len(g[v])):
        if not u[g[v][i]]:
            dfs(g[v][i])
            dsu_unite(v, g[v][i], v)
    for i in range(len(q[v])):
        if u[q[v][i]]:
            print(f"{v + 1} {q[v][i] + 1} -> {ancestor[dsu_get(q[v][i])] + 1}")

# Чтение графа
# ... (замените на соответствующий код)

# Чтение запросов
while True:
    a, b = map(int, input().split())  # очередной запрос
    a, b = a - 1, b - 1
    q[a].append(b)
    q[b].append(a)

# Обход в глубину и ответ на запросы
dfs(0)
