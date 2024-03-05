class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def find_tree_height(node):
    if not node:
        return 0

    child_heights = [find_tree_height(child) for child in node.children]
    return 1 + max(child_heights, default=0)


n = int(input())
s = list(map(int, input().split()))
nodes = [TreeNode(i) for i in range(n)]
for i in range(1, n):
    parent_index = s[i - 1]
    nodes[parent_index].children.append(nodes[i])

root = nodes[0]
height = find_tree_height(root) - 1

h = sorted(find_tree_height(node) for node in root.children)
if len(h) == 1:
    d = h[0]
else:
    d = h[-2] + h[-1]

print(height, d)


distances = [-1] * n
distances[root.value] = 0
queue = [root]

while queue:
    current = queue.pop(0)

    for child in current.children:
        if distances[child.value] == -1:
            distances[child.value] = distances[current.value] + 1
            queue.append(child)

print(*distances)
