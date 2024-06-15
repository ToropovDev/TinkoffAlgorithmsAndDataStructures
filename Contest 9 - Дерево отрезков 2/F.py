# Сад пермского периода
import sys


class Center:
    def __init__(self, _x, _y, _id):
        self.x = _x
        self.y = _y
        self.id = _id


n = int(sys.stdin.readline().split()[2])
centers = []
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    centers.append(Center(int(x * 2), int(y * 2), i))

y = [center.y for center in centers]
y.sort()
y = list(dict.fromkeys(y))

centers.sort(key=lambda center: center.x)
x = [0] * len(y)


def get_x(_index):
    sum_val = 0
    while _index >= 0:
        sum_val += x[_index]
        _index = (_index & (_index + 1)) - 1
    return sum_val


def add_since_x(_index, extra):
    while _index < len(x):
        x[_index] += extra
        _index |= (_index + 1)


def add_range_x(_first, _after, extra):
    if _first is not None:
        add_since_x(_first, extra)
    if _after is not None:
        add_since_x(_after, -extra)


ans = [0] * n
for center in centers:
    index = y.index(center.y)
    dist = center.x - get_x(index)
    assert dist > 0
    assert ans[center.id] == 0
    ans[center.id] = dist
    first = next((i for i, val in enumerate(y) if val > center.y - dist), None)
    after = next((i for i, val in enumerate(y) if val > center.y + dist), None)
    add_range_x(first, after, dist * 2)

for value in ans:
    assert value != 0
    sys.stdout.write(str(value) + ' ')
