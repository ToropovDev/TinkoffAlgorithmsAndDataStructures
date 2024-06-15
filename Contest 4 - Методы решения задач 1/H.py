# Межрегиональная олимпиада
from bisect import bisect_left


class Problem:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end


n, c = map(int, input().split())
problems = []
for _ in range(n):
    start, time = map(int, input().split())
    problems.append(Problem(start, start + time))

x = []
for p in problems:
    x.append(p.begin)
    x.append(p.end)

x = sorted(set(x))
l = len(x)

for p in problems:
    p.begin = bisect_left(x, p.begin)
    p.end = bisect_left(x, p.end)

starts = [[] for _ in range(l)]
for i, p in enumerate(problems):
    starts[p.begin].append(i)

sums = [0] * l
used = [-1] * l
for t in range(l):
    if t > 0:
        if sums[t] <= sums[t - 1]:
            sums[t] = sums[t - 1]
            used[t] = -1
    for pid in starts[t]:
        p = problems[pid]
        if sums[p.end] < sums[p.begin] + c:
            sums[p.end] = sums[p.begin] + c
            used[p.end] = pid

ans = []
for t in range(l):
    pid = used[t]
    if pid != -1:
        ans.append(pid)

print(sums[-1])
print(len(ans))
print(*[pid + 1 for pid in ans])
