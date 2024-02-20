# C-Отгадай число
import sys

n = int(input())


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


l, r = 1, n + 1
while r - l > 1:
    mid = (l + r) // 2
    inp = query(mid)
    if inp == "<":
        r = mid
    elif inp == ">=":
        l = mid
print(f"! {l}")