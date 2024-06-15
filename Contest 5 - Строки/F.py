# Подпалиндромы


def manacher(s):
    s = '#' + '#'.join(s) + '#'
    n = len(s)
    radius = [0] * n
    center = right = 0
    count = 0

    for i in range(n):
        if i < right:
            radius[i] = min(right - i, radius[2 * center - i])
        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < n and s[i - radius[i] - 1] == s[i + radius[i] + 1]:
            radius[i] += 1
        count += (radius[i] + 1) // 2

        if i + radius[i] > right:
            center, right = i, i + radius[i]

    return count


s = input()
result = manacher(s)
print(result)
