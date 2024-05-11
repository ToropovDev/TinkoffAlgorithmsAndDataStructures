MOD = 10 ** 9 + 7


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = (fact * i) % MOD
    return fact


def mod_inverse(n):
    return pow(n, MOD - 2, MOD)


def binomial_coefficient(n, k):
    numerator = factorial(n)
    denominator = (factorial(k) * factorial(n - k)) % MOD
    return (numerator * mod_inverse(denominator)) % MOD


n, k = map(int, input().split())
result = binomial_coefficient(n, k)
print(result)
