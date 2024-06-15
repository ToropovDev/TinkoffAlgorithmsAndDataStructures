# Разложение на простые

n = int(input())

result = []
i = 2
while i * i <= n:
    c = 0
    while n % i == 0:
        n //= i
        c += 1
    if c == 1:
        result += [str(i)]
    elif c > 1:
        result += [f"{i}^{c}"]
    i += 1

if n > 1:
    result += [str(n)]
print("*".join(result))
