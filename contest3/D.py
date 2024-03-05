def heap_up(arr, i):
    while i > 0 and arr[(i - 1) // 2] < arr[i]:
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2


def heap_down(arr, i):
    while i * 2 + 2 < len(arr):
        if arr[2 * i + 1] <= arr[i] and arr[2 * i + 2] <= arr[i]:
            break
        else:
            if arr[2 * i + 1] > arr[2 * i + 2]:
                arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
                i = 2 * i + 1
            else:
                arr[i], arr[2 * i + 2] = arr[2 * i + 2], arr[i]
                i = 2 * i + 2
    if 2 * i + 1 < len(arr) and arr[2 * i + 1] > arr[i]:
        arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]


n = int(input())
arr = []

for i in range(n):
    x = input().split()

    if len(x) == 1:
        print(arr[0])
        arr[0] = arr[len(arr) - 1]
        arr.pop()
        heap_down(arr, 0)
    else:
        tmp = int(x[1])
        arr.append(tmp)
        heap_up(arr, len(arr) - 1)
