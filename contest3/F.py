import random


class Item:
    key: int
    priority: int
    def __init(self, key, priority):
        self.key = key
        self.priority = priority
        self.l = None
        self.r = None


def split(t: Item, key, l: Item, r: Item):
    if not t:
        l = r = None
    elif key <= t.key:
        split(t.l, key, l, t.l)
        r = t
    else:
        split(t.r, key, t.r, r)
        l = t


def merge(l: Item, r: Item, t: Item):
    if not l or not r:
        t = l if l else r
    elif l.priority > r.priority:
        merge(l.r, r, l.r)
        t = l
    else:
        merge(l, r.l, r.l)
        t = r


def GetMin(t: Item):
    if t is None:
        return -1
    if t.l is None:
        return t.key
    return GetMin(t.l)


def add(i):
    split(tree, i, L, R)
    if GetMin(R) != i:
        merge(l, Item(i, random.randint), tree)
        merge(tree, R, tree)
    else:
        merge(L, R, tree)


def next(i):
