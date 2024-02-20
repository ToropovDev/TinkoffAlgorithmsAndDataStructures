# I-Что? Да! Пузырек

# в процессе

def bubble_sort_iterations(arr):
    n = len(arr)
    iterations = 0
    for i in range(n):
        had_swaps = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                had_swaps = True
        iterations += 1
        if not had_swaps:
            break
    return iterations


n = int(input())
positions = list(map(int, input().split()))

arr = [0] * n
result = []

for pos in positions:
    arr[pos - 1] = 1
    iterations = bubble_sort_iterations(arr.copy())
    result.append(iterations)

result.insert(0, bubble_sort_iterations(arr))
print(*result)
