# Расстояние Дамерау-Левенштейна

s1 = input()
s2 = input()

n = len(s1)
m = len(s2)
matrix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    matrix[i][0] = i
for j in range(m + 1):
    matrix[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = 0 if s1[i - 1] == s2[j - 1] else 1

        matrix[i][j] = min(matrix[i - 1][j] + 1,
                           matrix[i][j - 1] + 1,
                           matrix[i - 1][j - 1] + cost)

        if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
            matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + cost)

print(matrix[n][m])
