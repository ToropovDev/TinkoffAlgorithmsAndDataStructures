import sys


def print_result(dp, pred, s, i, j):
    if dp[i][j] == j - i + 1:
        pass
    elif dp[i][j] == 0:
        for h in range(i, j + 1):
            print(s[h], end='')
    elif pred[i][j] == -1:
        print(s[i], end='')
        print_result(dp, pred, s, i + 1, j - 1)
        print(s[j], end='')
    else:
        print_result(dp, pred, s, i, pred[i][j])
        print_result(dp, pred, s, pred[i][j] + 1, j)


def check():
    return (
            (s[i] == '(' and s[j] == ')')
            or (s[i] == '[' and s[j] == ']')
            or (s[i] == '{' and s[j] == '}')
            )


s = input()
n = len(s)

dp = [[0] * n for _ in range(n)]
pred = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for j in range(n):
    for i in range(j - 1, -1, -1):
        current = dp[i + 1][j - 1] if check() else sys.maxsize
        p = -1
        for k in range(i, j):
            if dp[i][k] + dp[k + 1][j] < current:
                current = dp[i][k] + dp[k + 1][j]
                p = k
        dp[i][j] = current
        pred[i][j] = p

print_result(dp, pred, s, 0, n - 1)
