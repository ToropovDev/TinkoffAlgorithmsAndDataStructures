# D-Шарики

n = int(input())
result = 0
arr = list(map(int, input().split()))
stack = [arr[0]]

for i in range(1, n + 1):
    if i < n:
        x = arr[i]
        if x == stack[-1]:
            stack.append(x)
            continue

    l = len(stack) - 1
    while l >= 0 and stack[l] == stack[-1]:
        l -= 1
    c = len(stack) - l - 1

    if c >= 3:
        for j in range(c):
            stack.pop()
        result += c

    if i < n:
        stack.append(arr[i])

print(result)
