# A-Суммы и XOR-ы на отрезках

n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
s = [0] * (n + 1)
k = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i]
    k[i] = k[i - 1] ^ a[i]

result = []

for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        if l > 0:
            result.append(s[r] - s[l - 1])
        else:
            result.append(s[r])
    else:
        if l > 0:
            result.append(k[r] ^ k[l - 1])
        else:
            result.append(k[r])

for elem in result:
    print(elem)
