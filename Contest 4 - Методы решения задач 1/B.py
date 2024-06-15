# B-2D суммы

n, m, k = map(int, input().split())

a = [[0] * m for _ in range(n)]
s = [[0] * m for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

s[0][0] = a[0][0]

for i in range(1, n):
    s[i][0] = s[i - 1][0] + a[i][0]

for i in range(1, m):
    s[0][i] = s[0][i - 1] + a[0][i]

for i in range(1, n):
    for j in range(1, m):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j]


def query(x1, y1, x2, y2):
    return s[x2][y2] - (s[x1 - 1][y2] if x1 > 0 else 0) - (s[x2][y1 - 1] if y1 > 0 else 0) + (
        s[x1 - 1][y1 - 1] if x1 > 0 and y1 > 0 else 0)


result = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(query(x1 - 1, y1 - 1, x2 - 1, y2 - 1))

for elem in result:
    print(elem)
