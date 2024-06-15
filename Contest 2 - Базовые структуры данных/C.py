# Постфиксная запись

expr = input().split()
res = []
for s in expr:
    if s.isdigit():
        res += [s]
    else:
        el = res.pop()
        res.append(eval(f'{res.pop()}{s}{el}'))
print(res[-1])
