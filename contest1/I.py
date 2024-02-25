# I-Что? Да! Пузырек

n = int(input())
positions = list(map(int, input().split()))


arr = [0] * n
result = [1]
for j in range(n-1):
    arr[positions[j] - 1] += 1
    if arr[-1] == 0:
        result.append(j+2)
    else:
        r = 0
        c = n-1
        while c > -1 and arr[c] == 1:
            r += 1
            c -= 1
        result.append(j+2-r)

result.append(1)
print(*result)

# 0 0 0 0 - 1
# 1 0 0 0 - 2
# 1 0 1 0 - 3
# 1 0 1 1 - 2
# 1 1 1 1 - 1
