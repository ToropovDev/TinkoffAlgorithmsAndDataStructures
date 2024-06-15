# Монетки

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a) * 2
res = []


def f(pos=0, _sum=0, current=None):
    if current is None:
        current = []
    global res
    if pos == m:
        if _sum == n:
            if not res or len(current) < len(res):
                res = current.copy()
            return
        return
    f(pos + 1, _sum, current)
    f(pos + 1, _sum + a[pos], current + [a[pos]])
    f(pos + 1, _sum + a[pos] * 2, current + [a[pos], a[pos]])


if s < n:
    print(-1)
else:
    f()
    if not res:
        print(0)
    else:
        print(len(res))
        print(*res)
