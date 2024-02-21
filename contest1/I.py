n = int(input())


def bubble_sort_iterations(arr):
    if 0 in arr:
        j = n - arr[::-1].index(0)
        return arr[:j].count(1) + 1
    else:
        return 1


positions = [int(num) for num in input().split()]

arr = [0] * n
result = [1] * (n+1)
result[0] = bubble_sort_iterations(arr)
for i in range(n-1):
    arr[positions[i] - 1] = 1
    result[i+1] = bubble_sort_iterations(arr)

print(*result)
