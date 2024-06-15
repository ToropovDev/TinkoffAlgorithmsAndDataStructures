# C-Коровы --- в стойла

n, k = map(int, input().split())
s = sorted(list(map(int, input().split())))

l, r = 0, s[-1] - s[0] + 1
while l < r:
    mid = (l + r) // 2
    cows = 1
    last = s[0]
    for el in s[1:]:
        if el - last > mid:
            cows += 1
            last = el
    if cows >= k:
        l = mid + 1
    else:
        r = mid

print(l)
