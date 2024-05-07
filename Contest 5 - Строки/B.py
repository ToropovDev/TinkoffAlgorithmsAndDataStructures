def get_prefix(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = get_prefix(pattern)
    q = 0
    indices = []
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            indices.append(i - m + 1)
            q = pi[q - 1]
    return indices


T = input().strip()
q = int(input().strip())
queries = [input().strip() for _ in range(q)]

for query in queries:
    indices = kmp(T, query)
    print(len(indices), *indices)
