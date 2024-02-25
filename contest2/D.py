# D-Шарики

# надо бы оптимизировать

n = int(input())
arr = list(map(int, input().split()))

while arr:
    repeat_ind = [0]
    last = arr[0]
    i = 1

    while i < len(arr):
        ball = arr[i]
        if last != ball:
            if len(repeat_ind) >= 3:
                break
            repeat_ind.clear()
        repeat_ind.append(i)
        last = ball
        i += 1

    if len(repeat_ind) < 3:
        break

    for i in range(len(repeat_ind)):
        arr.pop(repeat_ind[0])

print(n - len(arr))
