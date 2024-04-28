import sys

class SegmentTree:
    def __init__(self, src):
        self.tree = [0] * (4 * len(src))
        self.build(src, 1, 0, len(src) - 1)

    def build(self, src, v, tl, tr):
        if tl == tr:
            self.tree[v] = src[tl]
        else:
            tm = (tl + tr) // 2
            self.build(src, v * 2, tl, tm)
            self.build(src, v * 2 + 1, tm + 1, tr)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])

    def get_min_index(self, v, tl, tr, l, r, x):
        if l > r:
            return sys.maxsize

        if tl == tr:
            return tl if self.tree[v] >= x else sys.maxsize

        tm = (tl + tr) // 2

        if tl < l:
            return min(
                self.get_min_index(v * 2, tl, tm, l, min(r, tm), x),
                self.get_min_index(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)
            )

        if self.tree[v * 2] >= x:
            return self.get_min_index(v * 2, tl, tm, l, min(r, tm), x)
        else:
            return self.get_min_index(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r, x)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos, new_val)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])


n, m = map(int, input().split())
a = list(map(int, input().split()))

tree = SegmentTree(a)
result_list = []

for _ in range(m):
    operation, *args = map(int, input().split())
    if operation == 1:
        i, v = args
        tree.update(1, 0, n - 1, i, v)
    else:
        x, l = args
        res = tree.get_min_index(1, 0, n - 1, l, n - 1, x)
        result_list.append(res if res != sys.maxsize else -1)

for i in result_list:
    print(i)

