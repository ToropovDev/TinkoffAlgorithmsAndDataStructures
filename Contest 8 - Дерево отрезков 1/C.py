# K-я единица


class SegmentTree:
    def __init__(self, src):
        self.tree = [0] * (4 * len(src))
        self.build(src, 1, 0, len(src) - 1)

    def build(self, src, v, tl, tr):
        if tl == tr:
            self.tree[v] = int(src[tl] == 1)
        else:
            tm = (tl + tr) // 2
            self.build(src, v * 2, tl, tm)
            self.build(src, v * 2 + 1, tm + 1, tr)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

    def get_k_one(self, v, tl, tr, k):
        if tl == tr:
            return tl

        tm = (tl + tr) // 2
        if k <= self.tree[v * 2]:
            return self.get_k_one(v * 2, tl, tm, k)
        else:
            return self.get_k_one(v * 2 + 1, tm + 1, tr, k - self.tree[v * 2])

    def update(self, v, tl, tr, pos):
        if tl == tr:
            self.tree[v] = 1 - self.tree[v]
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(v * 2, tl, tm, pos)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]


n, m = map(int, input().split())
a = list(map(int, input().split()))

seg_tree = SegmentTree(a)
result_list = []

for _ in range(m):
    operation, *args = input().split()
    if operation == '1':
        i = int(args[0])
        seg_tree.update(1, 0, n - 1, i)
    else:
        k = int(args[0])
        result = seg_tree.get_k_one(1, 0, n - 1, k + 1)
        result_list.append(result)

for i in result_list:
    print(i)