class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n)

    def build(self, arr, v, tl, tr):
        if tl == tr - 1:
            self.tree[v] = arr[tl]
        else:
            tm = (tl + tr) // 2
            self.build(arr, 2 * v + 1, tl, tm)
            self.build(arr, 2 * v + 2, tm, tr)
            self.tree[v] = self.tree[2 * v + 1] + self.tree[2 * v + 2]

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr - 1:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos < tm:
                self.update(2 * v + 1, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 2, tm, tr, pos, new_val)
            self.tree[v] = self.tree[2 * v + 1] + self.tree[2 * v + 2]

    def query(self, v, tl, tr, l, r):
        if l >= r:
            return 0
        if tl == l and tr == r:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self.query(2 * v + 1, tl, tm, l, min(r, tm)) + self.query(2 * v + 2, tm, tr, max(l, tm), r)


n, m = map(int, input().split())
a = list(map(int, input().split()))

tree = SegmentTree(a)

for _ in range(m):
    operation, *args = map(int, input().split())
    if operation == 1:
        i, v = args
        tree.update(0, 0, n, i, v)
    elif operation == 2:
        l, r = args
        print(tree.query(0, 0, n, l, r))
