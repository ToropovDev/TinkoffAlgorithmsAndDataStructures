# H-Зеркальный код

# в процессе

def h(s):
    result = ""
    counter = []
    for el in sorted(set(s)):
        counter += [[el, s.count(el)]]

    for pair in counter:
        result += pair[0] * (pair[1] // 2)
        pair[1] %= 2

    counter = [pair for pair in counter if pair[1] != 0]
    if len(counter) == 0:
        return result+result[::-1]
    else:
        return result+counter[0][0]+result[::-1]


n = int(input())
s = input()

print(h(s))

assert h("AAB") == "ABA"
assert h("QAZQAZ") == "AQZZQA"
assert h("QAZQAZS") == "AQZSZQA"
assert h("QAZQAZSA") == "AQZAZQA"
assert h("AAAAAQQS") == "AAQAQAA"
