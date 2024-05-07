# E-Корень кубического уравнения
a, b, c, d = map(int, input().split())

r = 1e18
l = -r


def f(x):
    return a*x*x*x+b*x*x+c*x+d


while r - l > 1e-12:
    m = (l + r) / 2
    if f(m) * f(r) > 0:
        r = m
    else:
        l = m

print(l)
