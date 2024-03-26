# работает, но лучше переписать на c++

PRIME = 1000000009


def get_hash(l, r):
    return hashes[r + 1] - hashes[l] * prime_pows[r - l + 1]


def check_substrings(a, b, c, d):
    return get_hash(a, b) == get_hash(c, d)


s = input()
m = int(input())

hashes = [0] * (len(s) + 1)
prime_pows = [1] * (len(s) + 1)
res = []

hashes[0] = 0

for i in range(len(s)):
    hashes[i + 1] = hashes[i] * PRIME + ord(s[i])
    prime_pows[i + 1] = prime_pows[i] * PRIME

for i in range(m):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    res.append("Yes" if check_substrings(a, b, c, d) else "No")

for r in res:
    print(r)
