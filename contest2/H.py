# H-Хорошие дни

def nearest_smaller_left(n, arr):
    res = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)

    return res


n = int(input())
arr = list(map(int, input().split()))
result = nearest_smaller_left(n, arr)
print(result)
