# Присваивание, прибавление и сумма


class Node:
    def __init__(self):
        self.summa = 0
        self.add = 0
        self.replace = -1


def push_tree(tree, v, tree_size):
    if tree[v].replace != -1:
        if tree_size != 1:
            tree[v * 2].replace = tree[v * 2 + 1].replace = tree[v].replace
            tree[v * 2].add = tree[v * 2 + 1].add = 0
        tree[v].summa = tree[v].replace * tree_size

    tree[v].replace = -1

    if tree_size != 1:
        tree[v * 2].add += tree[v].add
        tree[v * 2 + 1].add += tree[v].add
    tree[v].summa += tree[v].add * tree_size
    tree[v].add = 0


def get_sum(tree, v, tl, tr, l, r):
    push_tree(tree, v, tr - tl + 1)

    if l > r:
        return 0

    if l == tl and tr == r:
        return tree[v].summa

    tm = (tl + tr) // 2
    return (get_sum(tree, v * 2, tl, tm, l, min(r, tm))
            + get_sum(tree, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r))


def update_replace(tree, v, tl, tr, l, r, value):
    push_tree(tree, v, tr - tl + 1)

    if l > r:
        return

    if l == tl and tr == r:
        tree[v].replace = value
        tree[v].add = 0
        push_tree(tree, v, tr - tl + 1)

    else:
        tm = (tl + tr) // 2
        update_replace(tree, v * 2, tl, tm, l, min(r, tm), value)
        update_replace(tree, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, value)
        tree[v].summa = tree[v * 2].summa + tree[v * 2 + 1].summa


def update_add(tree, v, tl, tr, l, r, value):
    push_tree(tree, v, tr - tl + 1)

    if l > r:
        return

    if l == tl and tr == r:
        tree[v].add += value
        push_tree(tree, v, tr - tl + 1)

    else:
        tm = (tl + tr) // 2
        update_add(tree, v * 2, tl, tm, l, min(r, tm), value)
        update_add(tree, v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, value)
        tree[v].summa = tree[v * 2].summa + tree[v * 2 + 1].summa


n, m = map(int, input().split())

tree = [Node() for _ in range(n * 4)]
result_list = []

for _ in range(m):
    operation, *args = map(int, input().split())
    if operation == 1:
        l, r, v = args
        update_replace(tree, 1, 0, n - 1, l, r - 1, v)

    elif operation == 2:
        l, r, v = args
        update_add(tree, 1, 0, n - 1, l, r - 1, v)

    else:
        l, r = args
        result_list.append(get_sum(tree, 1, 0, n - 1, l, r - 1))

for r in result_list:
    print(r)
