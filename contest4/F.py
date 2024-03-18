# F-Закраска прямой

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

s = sorted(s, key=lambda x: (x[0], x[1]))
c, result = s[0], 0

for i in range(1, n):
    if s[i][1] >= c[1]:
        if s[i][0] > c[1]:
            result += c[1] - c[0]
            c = s[i]
        if s[i][0] <= c[1]:
            c[1] = s[i][1]
result += c[1] - c[0]

print(result)
