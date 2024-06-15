# Вика и отрезки

MAXN = 1000005

n = int(input())
st = [0] * (MAXN << 2)
lazy = [0] * (MAXN << 2)
old = [0] * (MAXN << 2)
v = []
sor = []

def pull(index, left, right):
    if lazy[index]:
        st[index] = old[index]
    elif left == right:
        st[index] = 0
    else:
        st[index] = st[index << 1 | 1] + st[index << 1]

def insert(index, start, end, left, right, k):
    if left <= start and end <= right:
        lazy[index] += k
        pull(index, start, end)
        return
    middle = (start + end) // 2
    if left <= middle:
        insert(index << 1, start, middle, left, right, k)
    if middle < right:
        insert(index << 1 | 1, middle + 1, end, left, right, k)
    pull(index, start, end)

def input_(index, left, right):
    if left == right:
        old[index] = sor[left] - sor[left - 1] if left > 0 else sor[left]
        return
    mid = (left + right) // 2
    input_(index << 1, left, mid)
    input_(index << 1 | 1, mid + 1, right)
    old[index] = old[index << 1] + old[index << 1 | 1]

for _ in range(n):
    a, b, c, f = map(int, input().split())
    if a == c and b == f:
        left = a
        right = a + 1
        bottom = b
        top = b + 1
    elif a == c:
        left = a
        right = a + 1
        bottom = min(b, f)
        top = max(b, f) + 1
    else:
        left = min(a, c)
        right = max(a, c) + 1
        bottom = b
        top = b + 1

    sor.extend([bottom, top])
    v.append((left, bottom, top, 1))
    v.append((right, bottom, top, -1))

sor = list(set(sor))
sor.sort()
for i in range(len(v)):
    a, b, c, k = v[i]
    v[i] = (a, sor.index(b), sor.index(c), k)

input_(1, 1, len(sor) - 1)
v.sort()
pre = 0
ans = 0
for pos, a, b, k in v:
    if pre != pos:
        ans += (pos - pre) * st[1]
        pre = pos
    insert(1, 1, len(sor) - 1, a + 1, b, k)

print(ans)
