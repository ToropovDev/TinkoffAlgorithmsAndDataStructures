# E-Сортировка вагонов

# какая-то странная фигня

s = []
op = []
n = int(input())
num = 1
for i in range(n):
    val = int(input())
    if len(s) > 0 and val > s[len(s) - 1]:
        print(0)
        quit(0)
    op.append(1)
    s.append(val)
    while len(s) > 0 and s[len(s) - 1] == num:
        op.append(2)
        s.pop()
        num += 1
val = op.pop(0)
count = 1
while len(op) > 0:
    if op[0] == val:
        count += 1
    else:
        print("{0} {1}".format(val, count))
        val = op[0]
        count = 1
    op.pop(0)
print("{0} {1}".format(val, count))