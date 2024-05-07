import sys


def get_min(tree, v, tl, tr, l, r):
    if l > r:
        return sys.maxsize

    additional = tree[v][1]

    if l == tl and tr == r:
        return tree[v][0] + additional

    tm = (tl + tr) // 2
    return min(
        get_min(tree, v * 2, tl, tm, l, min(r, tm)),
        get_min(tree, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
    ) + additional


def update(tree, v, tl, tr, l, r, value):
    if l > r:
        return

    if l == tl and tr == r:
        tree[v] = (tree[v][0], tree[v][1] + value)
    else:
        tm = (tl + tr) // 2
        update(tree, v * 2, tl, tm, l, min(r, tm), value)
        update(tree, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, value)
        tree[v] = (
            min(tree[v * 2][0] + tree[v * 2][1], tree[v * 2 + 1][0] + tree[v * 2 + 1][1]),
            tree[v][1]
        )


n, m = map(int, input().split())

tree = [(0, 0) for _ in range(n * 4)]
result_list = []
for _ in range(m):
    operation, *params = map(int, input().split())
    if operation == 1:
        l, r, v = params
        update(tree, 1, 0, n - 1, l, r - 1, v)
    else:
        l, r = params
        result_list.append(get_min(tree, 1, 0, n - 1, l, r - 1))

for r in result_list:
    print(r)
