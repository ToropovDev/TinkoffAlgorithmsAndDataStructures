# A-Двоичный поиск
n, k = map(int, input().split())
arr = [int(d) for d in input().split()]
arr2 = [int(d) for d in input().split()]


def binary_search(m):
    l, r = 0, n
    while r - l > 1:
        mid = (l + r) // 2
        if arr[mid] > m:
            r = mid
        else:
            l = mid
    return "YES" if arr[l] == m else "NO"


for i in range(k):
    print(binary_search(arr2[i]))
