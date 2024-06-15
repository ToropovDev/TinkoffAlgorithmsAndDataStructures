# Наибольшая возрастающая подпоследовательность


def get_result(n, a):
    dp = [1] * n
    prev_index = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev_index[i] = j

    max_l = max(dp)
    max_i = dp.index(max_l)

    result = []
    while max_i != -1:
        result += [(a[max_i])]
        max_i = prev_index[max_i]

    result = result[::-1]
    return max_l, result


n = int(input())
arr = list(map(int, input().split()))

length, subsequence = get_result(n, arr)

print(length)
print(*subsequence)
