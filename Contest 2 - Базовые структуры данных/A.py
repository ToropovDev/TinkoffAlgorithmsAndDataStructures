# A-Минимум на стеке

class Stack:
    def __init__(self, size=10000000):
        self.m = [0] * size
        self.size = 0

    def push(self, x):
        if self.size == 0:
            self.m[self.size] = x
            self.size += 1
        else:
            pos = self.size - 1
            self.m[self.size] = min(x, self.m[pos])
            self.size += 1

    def pop(self):
        self.size -= 1

    def get_min(self):
        return self.m[self.size - 1]


s = Stack()
n = int(input())
for i in range(n):
    op = list(map(int, input().split()))
    if op[0] == 1:
        x = op[1]
        s.push(x)
    elif op[0] == 2:
        s.pop()
    else:
        min_value = s.get_min()
        print(min_value)
