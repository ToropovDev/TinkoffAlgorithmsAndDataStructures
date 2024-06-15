# Длина максимального подпалиндрома


def find_longest_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for k in range(2, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and k == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    max_len = dp[0][n - 1]

    palindrome = ""
    i, j = 0, n - 1
    while i < j:
        if s[i] == s[j]:
            palindrome += s[i]
            i += 1
            j -= 1
        elif dp[i][j - 1] > dp[i + 1][j]:
            j -= 1
        else:
            i += 1
    second_part = palindrome
    if i == j:
        palindrome += s[i]
    palindrome += second_part[::-1]

    return max_len, palindrome


input_string = input().strip()
max_length, max_palindrome = find_longest_palindrome(input_string)
print(max_length)
print(max_palindrome)
