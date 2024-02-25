# J-Разбиение таблицы

import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nm = n * m
    best = 1e18
    ax = 'V'
    res = 0
    total_sum = nm * (nm + 1) // 2

    split = int((math.sqrt(nm * nm + m * m + 2 * nm + 1) - nm + m - 1) // 2)

    for i in range(split, min(m, split + 1) + 1):
        s = i * n * (i + 1 + nm - m) // 2
        diff = abs(s - (total_sum - s))
        if best > diff:
            best = diff
            ax = 'V'
            res = i

    split = int((math.sqrt(2 * nm * nm + 2 * nm + 1) - 1) // 2 // m)

    for i in range(split, min(n, split + 1) + 1):
        s = (m * m * i * i + m * i) // 2
        diff = abs(s - (total_sum - s))
        if best > diff:
            best = diff
            ax = 'H'
            res = i

    print(ax, res + 1)
