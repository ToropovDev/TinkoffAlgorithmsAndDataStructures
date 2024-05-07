def check(p, t):
    res = []
    c = 0
    for i in range(len(t) - len(p) + 1):
        mis_count = 0
        for j in range(len(p)):
            if p[j] != t[i + j]:
                mis_count += 1
                if mis_count > 1:
                    break
        if mis_count <= 1:
            c += 1
            res.append(i + 1)
    return c, res


p = input().strip()
t = input().strip()

result_count, result_occurrences = check(p, t)
print(result_count)
print(*result_occurrences)
