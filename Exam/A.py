# Петя и CMS
import sys


def check(n, computers, mid) -> bool:
    tests_num = 0
    for t, b, y in computers:
        cycles_num = mid // (b * t + y)
        remaining = mid % (b * t + y)
        tests_num += cycles_num * b + min(b, remaining // t)

        if tests_num >= n:
            return True

    return tests_num >= n


def allocate(n, m, computers, min_time) -> list:
    packages = [0] * m
    remaining_packages = n
    for i in range(m):
        if remaining_packages == 0:
            break

        t, b, y = computers[i]
        cycles_num = min_time // (b * t + y)
        remaining = min_time % (b * t + y)

        max_tests = cycles_num * b + min(b, remaining // t)
        packages[i] = min(max_tests, remaining_packages)
        remaining_packages -= packages[i]

    return packages


n, m = map(int, input().split())
computers = []

for _ in range(m):
    t, b, y = map(int, input().split())
    computers.append((t, b, y))

left, right = 0, sys.maxsize
while left < right:
    middle = (left + right) // 2
    if check(n, computers, middle):
        right = middle
    else:
        left = middle + 1

min_time = left
alloc = allocate(n, m, computers, min_time)

print(min_time)
print(' '.join(map(str, alloc)))
