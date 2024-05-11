def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def get_time(n, m, k, MOD):
    total_combinations = pow(m, n, MOD)
    time_seconds = (total_combinations * mod_inverse(k, MOD)) % MOD
    return time_seconds


n, m, k, MOD = map(int, input().split())
result = get_time(n, m, k, MOD)
print(result)
