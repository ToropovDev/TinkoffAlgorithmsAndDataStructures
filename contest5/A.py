s = input()
m = int(input())

p = 10 ** 10
hashes = [0] * (len(s) + 1)
pows = [1] + [0] * (len(s))

for i in range(len(s)):
    hashes[i + 1] = hashes[i] * p + ord(s[i])
    pows[i + 1] = pows[i] * p


def get_hash(l, r):
    return hashes[r + 1] - hashes[l] * pows[r - l + 1]


def check_substrings(a, b, c, d):
    return get_hash(a, b) == get_hash(c, d)


res = []

for _ in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    res.append("Yes" if check_substrings(a, b, c, d) else "No")

for elem in res:
    print(elem)