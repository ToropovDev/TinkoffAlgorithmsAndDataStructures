# B-AVL?
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None


def h(node: Node):
    if node is None:
        return 0
    lh = h(node.l)
    rh = h(node.r)
    return max(lh, rh) + 1


def is_bst(node: Node, min_val, max_val):
    if node is None:
        return True
    if not min_val < node.value < max_val:
        return False

    return is_bst(node.l, min_val, node.value) and is_bst(node.r, node.value, max_val)


def is_balanced(node: Node):
    if node is None:
        return True
    lh = h(node.l)
    rh = h(node.r)

    return abs(lh - rh) <= 1 and is_balanced(node.l) and is_balanced(node.r)


n, r = map(int, input().split())
s = [tuple(map(int, input().split())) for i in range(n)]

nodes = [Node(i) for i in range(n)]
for i, (left, right) in enumerate(s):
    if left != -1:
        nodes[i].l = nodes[left]
    if right != -1:
        nodes[i].r = nodes[right]

root = nodes[r]
result = int(is_bst(root, float('-inf'), float('inf')) and is_balanced(root))
print(result)
