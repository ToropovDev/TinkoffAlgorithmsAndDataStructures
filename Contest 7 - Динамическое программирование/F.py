# Наибольший квадрат


def find_largest_square(n, m, matrix):
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    coord_x = 0
    coord_y = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
                    coord_x = i - max_side + 1
                    coord_y = j - max_side + 1

    return max_side, coord_x+1, coord_y+1


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

side, res_x, res_y = find_largest_square(n, m, matrix)
print(side)
print(res_x, res_y)
