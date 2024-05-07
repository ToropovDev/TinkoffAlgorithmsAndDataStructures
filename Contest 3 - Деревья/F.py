# F-Следующий

import random


def get_keys_min(node):
    return node.keysMin if node else 1 << 30


class Treap:
    class TreapNode:
        def __init__(self, key):
            self.key = key
            self.priority = random.randint(0, 10 ** 9)
            self.keysMin = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def update(self, node):
        if node:
            node.keysMin = min(node.key, min(get_keys_min(node.left), get_keys_min(node.right)))

    def merge(self, a, b):
        if not a or not b:
            return a if a else b
        if a.priority > b.priority:
            a.right = self.merge(a.right, b)
            self.update(a)
            return a
        else:
            b.left = self.merge(a, b.left)
            self.update(b)
            return b

    def split(self, t, split_key):
        if not t:
            return None, None
        if t.key < split_key:
            t.right, b = self.split(t.right, split_key)
            a = t
        else:
            a, t.left = self.split(t.left, split_key)
            b = t
        self.update(a)
        self.update(b)
        return a, b

    def insert_unique(self, key):
        t_less, t_greater = self.split(self.root, key)
        t_equal, t_greater = self.split(t_greater, key + 1)
        if not t_equal:
            t_equal = self.TreapNode(key)
        self.root = self.merge(t_less, self.merge(t_equal, t_greater))

    def next(self, key):
        t_less, t_not_less = self.split(self.root, key)
        result = get_keys_min(t_not_less)
        self.root = self.merge(t_less, t_not_less)
        return result if result != 1 << 30 else -1


treap = Treap()

queries_count = int(input())
previous_result = 0

for _ in range(queries_count):
    query_type, key = input().split()
    key = int(key)
    if query_type == '+':
        treap.insert_unique((key + previous_result) % (10 ** 9))
        previous_result = 0
    else:
        previous_result = treap.next(key)
        print(previous_result)
