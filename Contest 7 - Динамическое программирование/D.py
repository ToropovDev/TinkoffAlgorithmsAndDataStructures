n, m = map(int, input().split())

arr = [[0] * (m + 3) for _ in range(n + 3)]
arr[2][2] = 1
start1, start2 = 2, 2

while start1 < n + 1 or start2 < m + 1:
    if start2 == m + 1:
        start1 += 1
    else:
        start2 += 1

    i, j = start1, start2
    while i <= n + 1 and j >= 2:
        arr[i][j] = arr[i + 1][j - 2] + arr[i - 1][j - 2] + arr[i - 2][j - 1] + arr[i - 2][j + 1]
        i += 1
        j -= 1

print(arr[n + 1][m + 1])
