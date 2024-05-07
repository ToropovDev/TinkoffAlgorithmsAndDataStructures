# A-Примитивы

import sys

sys.setrecursionlimit(10**6)


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


def dfs(node, parent, depth, graph):
    if depth > graph['max_depth']:
        graph['max_depth'] = depth
        graph['farthest_node'] = node

    if node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor != parent:
                dfs(neighbor, node, depth + 1, graph)


def find_diameter(s):
    graph = {}
    for i, parent in enumerate(s):
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(i + 1)

        if i + 1 not in graph:
            graph[i + 1] = []
        graph[i + 1].append(parent)

    start_node = 0
    graph['max_depth'] = 0
    graph['farthest_node'] = 0
    dfs(start_node, None, 0, graph)

    start_node = graph['farthest_node']
    graph['max_depth'] = 0
    graph['farthest_node'] = 0
    dfs(start_node, None, 0, graph)

    return graph['max_depth']


d = find_diameter(s)

distances = [-1] * n
distances[root.value] = 0
queue = [root]

while queue:
    current = queue.pop(0)
    for child in current.children:
        if distances[child.value] == -1:
            distances[child.value] = distances[current.value] + 1
            queue.append(child)


print(height, d)
print(*distances)
