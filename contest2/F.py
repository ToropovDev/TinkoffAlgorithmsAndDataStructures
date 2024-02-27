# F-Астроград
n = int(input())
d = []
positions = {}
left_people_count = 0

result = []

for i in range(n):
    s = input().split()
    t = int(s[0])
    if t == 1:
        person_id = int(s[1])
        positions[person_id] = len(d) + left_people_count
        d.append(person_id)
    elif t == 2:
        d.pop(0)
        left_people_count += 1
    elif t == 3:
        d.pop()
    elif t == 4:
        q = int(s[1])
        result.append(positions[q] - left_people_count)
    else:
        result.append(d[0])

for r in result:
    print(r)