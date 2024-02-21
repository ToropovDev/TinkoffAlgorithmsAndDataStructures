# J-Разбиение таблицы

t = int(input())
arr = []
for i in range(t):
    n, m = map(int, input().split())
    arr += [[n, m]]


def get_sum(arr):
    res = 0
    for i in range(len(arr)):
        res += sum(arr[i])
    return res


def create_table(n, m):
    table = [[]] * n
    for j in range(0, n * m, m):
        table[j // m] = [j + k for k in range(1, m + 1)]
    return table


def get_cut(table):
    best_diff = 10e18
    best = 0
    for j in range(len(table) - 1):
        s1 = get_sum(table[:j + 1])
        s2 = get_sum(table[j + 1:])
        diff = abs(s1 - s2)
        if diff < best_diff:
            best_diff = diff
            best = j + 1
    return best+1, best_diff


for i in range(t):
    n, m = arr[i][0], arr[i][1]
    table = create_table(n, m)
    h_best = get_cut(table)
    table = [list(sublist) for sublist in list(zip(*table))]
    v_best = get_cut(table)

    if h_best[1] >= v_best[1]:
        print(f"V {v_best[0]}")
    else:
        print(f"H {h_best[0]}")

