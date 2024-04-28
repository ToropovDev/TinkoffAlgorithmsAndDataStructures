class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        self.n = n

    def update(self, x, v):
        i = x
        while i <= self.n:
            self.tree[i] += v
            i += i & -i

    def get_sum(self, x):
        s = 0
        while x > 0:
            s += self.tree[x]
            x -= x & -x
        return s

    def get(self, x):
        s = self.tree[x]
        z = x - (x & -x)
        x -= 1
        while x > z:
            s -= self.tree[x]
            x -= x & -x
        return s

    def scale(self, a):
        for i in range(1, self.n + 1):
            self.tree[i] *= a


n = int(input())
elements = list(map(int, input().split()))

unique_elements = sorted(set(elements))
unique_elements = {elem: i + 1 for i, elem in enumerate(unique_elements)}
elements = [unique_elements[x] for x in elements]
tree = SegmentTree(n)

greater = [0] * n
for i in range(n):
    greater[i] = i - tree.get_sum(elements[i])
    tree.update(elements[i], 1)

less = [0] * n
tree = SegmentTree(n)
for i in range(n - 1, -1, -1):
    less[i] = tree.get_sum(elements[i] - 1)
    tree.update(elements[i], 1)

res = 0
for i in range(n):
    res += greater[i] * less[i]

print(res)

