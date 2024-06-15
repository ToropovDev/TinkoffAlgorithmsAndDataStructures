# D-Таблица умножения

n, k = map(int, input().split())


def check(x, n):
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count


left, right = 1, n * n
while left < right:
    mid = (left + right) // 2
    if check(mid, n) < k:
        left = mid + 1
    else:
        right = mid

print(left)
