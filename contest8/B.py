def combine(a, b):
    if a[0] < b[0]:
        return a
    if a[0] > b[0]:
        return b
    return a[0], a[1] + b[1]


def build(tree, a, v, tl, tr):
    if tl == tr:
        tree[v] = (a[tl], 1)
    else:
        tm = (tl + tr) // 2
        build(tree, a, v * 2, tl, tm)
        build(tree, a, v * 2 + 1, tm + 1, tr)
        tree[v] = combine(tree[v * 2], tree[v * 2 + 1])


def get_min(tree, v, tl, tr, l, r):
    if l > r:
        return float('inf'), 0

    if l == tl and r == tr:
        return tree[v]

    tm = (tl + tr) // 2
    return combine(
        get_min(tree, v * 2, tl, tm, l, min(r, tm)),
        get_min(tree, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
    )


def update(tree, v, tl, tr, pos, new_val):
    if tl == tr:
        tree[v] = (new_val, 1)
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            update(tree, v * 2, tl, tm, pos, new_val)
        else:
            update(tree, v * 2 + 1, tm + 1, tr, pos, new_val)
        tree[v] = combine(tree[v * 2], tree[v * 2 + 1])


n, m = map(int, input().split())
a = list(map(int, input().split()))

tree = [(0, 0)] * (n * 4)
build(tree, a, 1, 0, n - 1)


result_list = []

for _ in range(m):
    operation, *args = input().split()
    if operation == '1':
        i, v = map(int, args)
        update(tree, 1, 0, n - 1, i, v)
    else:
        l, r = map(int, args)
        result = get_min(tree, 1, 0, n - 1, l, r - 1)
        result_list.append((result[0], result[1]))

for elem in result_list:
    print(elem[0], elem[1])
