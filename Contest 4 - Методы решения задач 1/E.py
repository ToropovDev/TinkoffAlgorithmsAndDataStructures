# E-Разделение массива

n, k = map(int, input().split())
a = list(map(int, input().split()))


def check(s, x):
    res, c = 0, 0

    for num in s:
        if c + num > x:
            c = 0
            res += 1
        if num > x:
            return float('inf')
        c += num

    if c:
        res += 1

    return res


left, right = 0, max(a) * len(a)
while left < right:
    middle = (left + right) // 2
    if check(a, middle) <= k:
        right = middle
    else:
        left = middle + 1

print(left)

