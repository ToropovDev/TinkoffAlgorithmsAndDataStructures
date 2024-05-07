# D-Квадратный корень и квадратный квадрат
c = float(input())
l, r = 0, 10e7
while r - l > 1e-7:
    mid = (l + r) / 2
    x = mid * mid + (mid + 1) ** 0.5
    if x >= c:
        r = mid
    else:
        l = mid

print(r)
