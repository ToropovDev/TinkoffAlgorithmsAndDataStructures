# B-Минимум на отрезке
from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = []
d = deque()

for i in range(n):
    if (len(d) > 0) and (d[0] <= i - k):
        d.popleft()

    while len(d) > 0 and arr[d[-1]] >= arr[i]:
        d.pop()

    d += [i]

    if i >= k - 1:
        result += [arr[d[0]]]

print(*result)
