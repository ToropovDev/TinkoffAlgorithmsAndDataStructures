# H-Зеркальный код

# в процессе

n = int(input())
s = sorted(input())
counter = dict()
for c in s:
    if c not in counter:
        counter[c] = 0
    counter[c] += 1
result = ""
for let in counter:
    result += let * (counter[let] // 2)
    counter[let] -= counter[let] // 2 * 2

counter = sorted([pair for pair in counter.items() if pair[1] != 0])
if len(counter) == 0:
    print(result+result[::-1])
else:
    print(result+counter[0][0]+result[::-1])
