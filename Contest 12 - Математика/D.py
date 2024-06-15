# Последняя цифра N!

n = int(input())
count_2, count_5 = 0, 0

for i in range(1, n + 1):
    cur = i
    while cur % 5 == 0:
        cur //= 5
        count_5 += 1
    while cur % 2 == 0:
        cur //= 2
        count_2 += 1

trailing_zeros = min(count_2, count_5)
result = 1

for i in range(1, n + 1):
    cur = i
    while cur % 2 == 0 or cur % 5 == 0:
        if cur % 2 == 0:
            cur //= 2
        else:
            cur //= 5
    result = (result * cur) % 10

for _ in range(count_2 - trailing_zeros):
    result = (result * 2) % 10

print(result)
