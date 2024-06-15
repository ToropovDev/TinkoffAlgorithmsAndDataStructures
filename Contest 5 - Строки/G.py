# Анаграммы-2
import sys
from collections import defaultdict
from random import randint


def get_max_common_subset(a, b, n, m):
    hashes_a = [0] * (n + 1)
    hashes_b = [0] * (m + 1)
    hashes = {}
    random = {}

    for i in range(1, n + 1):
        value = a[i - 1]
        hashes_a[i] = get_hash(hashes_a[i - 1], value, hashes, random)

    for i in range(1, m + 1):
        value = b[i - 1]
        hashes_b[i] = get_hash(hashes_b[i - 1], value, hashes, random)

    len_by_hash = defaultdict(int)

    for i in range(n):
        for j in range(i, n):
            hash_value = hashes_a[j + 1] - hashes_a[i]
            length = j - i + 1
            len_by_hash[hash_value] = max(len_by_hash[hash_value], length)

    ans = 0

    for i in range(m):
        for j in range(i, m):
            hash_value = hashes_b[j + 1] - hashes_b[i]
            ans = max(ans, len_by_hash[hash_value])

    return ans


def get_hash(prev_hash, value, hashes, random_hash):
    hash_val = hashes.get(value, int(randint(1, 100000) * 100000))
    random_val = random_hash.get(value, int(randint(1, 100000) * 100000))
    hashes[value] = hash_val
    random_hash[value] = random_val
    return prev_hash + (value + random_val) * hash_val + value * 31


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
print(get_max_common_subset(a, b, n, m))
