# E-Сортировка вагонов

n = int(input())
arr = list(map(int, input().split()))
stack = []
c = []
result = []
num = 1
for val in arr:
    if len(stack) > 0 and val > stack[len(stack) - 1]:
        print(0)
        quit(0)

    c.append(1)
    stack.append(val)
    while len(stack) > 0 and stack[len(stack) - 1] == num:
        c.append(2)
        stack.pop()
        num += 1

val = c.pop(0)
count = 1
while len(c) > 0:
    if c[0] == val:
        count += 1
    else:
        result.append("{0} {1}".format(val, count))
        val = c[0]
        count = 1
    c.pop(0)
result.append("{0} {1}".format(val, count))
print(len(result))
for r in result:
    print(r)
