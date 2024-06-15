# I-Что? Да! Пузырек

n = int(input())
positions = list(map(int, input().split()))

arr = [0] * n
result = [1]
r = 1
pointer = n - 1
for j in range(n - 1):
    arr[positions[j] - 1] += 1
    r += 1
    while arr[pointer] == 1:
        pointer -= 1
        r -= 1
    result.append(r)
result.append(1)
print(*result)
