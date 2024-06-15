# Минимальный сдвиг

s = input()
if s == '':
    print(s)
else:
    a = [s]
    for i in range(len(s)):
        a.append(s[i:] + s[:i])
    a.sort()
    print(a[0])
