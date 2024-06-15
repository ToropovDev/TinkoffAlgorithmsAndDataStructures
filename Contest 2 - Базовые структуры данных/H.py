# H-Хорошие дни

def max_sum_min_subarray(n, arr):
    prev_smaller = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            prev_smaller[i] = stack[-1]
        stack.append(i)

    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    right = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i - 1]

    res = 0
    for i in range(n):
        l = left[i] + 1
        r = right[i] - 1 if right[i] != -1 else n - 1
        res = max(res, arr[i] * (prefix_sums[r + 1] - prefix_sums[l] if l <= r else 0))

    return res


n = int(input())
arr = list(map(int, input().split()))
print(max_sum_min_subarray(n, arr))
