# G-Anti-qsort test

n = int(input())
p = list(range(1, n + 1))
for i in range(2, n):
    p[i // 2], p[i] = p[i], p[i // 2]

for elem in p:
    print(elem, end=" ")
