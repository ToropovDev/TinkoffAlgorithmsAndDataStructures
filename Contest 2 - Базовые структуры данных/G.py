# G-Гоблины и очереди

def equalize(l, r):
    while len(l) < len(r):
        l.append(r.pop(0))
    while len(l) > len(r) + 1:
        r.insert(0, l.pop())


n = int(input())
left, right = [], []
result = []

for i in range(n):
    s = input().split()
    t = s[0]
    if t == "+":
        right.append(int(s[1]))
    elif t == '*':
        left.append(int(s[1]))
    else:
        result.append(left[0])
        left.pop(0)

    equalize(left, right)

for r in result:
    print(r)
