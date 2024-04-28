def encode(i, j, sizeJ):
    return i * (sizeJ + 1) + j


def get_root(v, parent):
    if parent[v] < 0:
        return v
    else:
        root = get_root(parent[v], parent)
        parent[v] = root
        return root


def join(a, b, parent):
    a = get_root(a, parent)
    b = get_root(b, parent)
    if a == b:
        return False
    assert parent[a] < 0
    assert parent[b] < 0
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b
    return True


sizeI, sizeJ = map(int, input().split())
parent = [-1] * (encode(sizeI + 1, sizeJ + 1, sizeJ) + 1)

for i in range(1, sizeI + 1):
    code_str = input().split()
    for j in range(1, sizeJ + 1):
        code = int(code_str[j-1])
        if code & 1:
            join(encode(i, j, sizeJ), encode(i + 1, j, sizeJ), parent)
        if code & 2:
            assert j < sizeJ
            join(encode(i, j, sizeJ), encode(i, j + 1, sizeJ), parent)

ansI = []
ansJ = []
ansD = []
ansCost = 0

for i in range(1, sizeI):
    for j in range(1, sizeJ + 1):
        if join(encode(i, j, sizeJ), encode(i + 1, j, sizeJ), parent):
            ansI.append(i)
            ansJ.append(j)
            ansD.append(1)
            ansCost += 1

for i in range(1, sizeI + 1):
    for j in range(1, sizeJ):
        if join(encode(i, j, sizeJ), encode(i, j + 1, sizeJ), parent):
            ansI.append(i)
            ansJ.append(j)
            ansD.append(2)
            ansCost += 2

print(len(ansI), ansCost)
for i in range(len(ansI)):
    print(ansI[i], ansJ[i], ansD[i])
