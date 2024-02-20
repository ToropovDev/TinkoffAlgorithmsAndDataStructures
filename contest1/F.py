# F-Сортировка слиянием с приколом
n = int(input())
arr = list(map(int, input().split()))


def merge_sort(arr):
    inv = 0

    if len(arr) > 1:
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]
        inv += merge_sort(l)
        inv += merge_sort(r)

        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:

                arr[k] = l[i]
                i += 1
            else:
                inv += len(l) - i
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):

            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1

    return inv


print(merge_sort(arr))
for elem in arr:
    print(elem, end=" ")
