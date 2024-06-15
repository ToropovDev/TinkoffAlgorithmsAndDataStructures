# Гипотеза Гольдбаха


def generate_prime_nums(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


def goldbach(n):
    primes = generate_prime_nums(n)
    for p in primes:
        if p > n // 2:
            break
        if n - p in primes:
            return p, n - p


n = int(input())
print(*goldbach(n))
