# Упаковка символов

s = input().strip()
n = len(s)
packed = [[""] * n for _ in range(n)]

for length in range(1, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        min_str = s[left:right + 1]
        if length > 4:
            for right1 in range(left, right):
                left2 = right1 + 1
                t = packed[left][right1] + packed[left2][right]
                if len(t) < len(min_str):
                    min_str = t
            for p in range(1, length):
                if length % p == 0:
                    is_periodic = all(s[i] == s[i - p] for i in range(left + p, right + 1))
                    if is_periodic:
                        t = f"{length // p}({packed[left][left + p - 1]})"
                        if len(t) < len(min_str):
                            min_str = t
        packed[left][right] = min_str

print(packed[0][n - 1])
