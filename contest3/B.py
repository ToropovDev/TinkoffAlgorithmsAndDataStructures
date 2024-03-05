class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def check_avl(root):
    def check_avl_conditions(node):
        if not node:
            return True, 0

        l_check, lh = check_avl_conditions(node.left)
        r_check, rh = check_avl_conditions(node.right)

        current_height = max(lh, rh) + 1
        height_difference = abs(lh - rh)

        check = l_check and r_check and height_difference <= 1
        is_sorted = (node.left is None or node.left.value < node.value) and \
                    (node.right is None or node.right.value > node.value)

        return check and is_sorted, current_height

    is_avl, _ = check_avl_conditions(root)
    return is_avl


n, r = map(int, input().split())

if n == 0:
    print(0)

else:

    nodes = [Node(i) for i in range(n)]

    for i in range(n):
        l, ri = map(int, input().split())
        if l != -1:
            nodes[i].left = nodes[l]
        if ri != -1:
            nodes[i].right = nodes[ri]

    root = nodes[r]

    result = check_avl(root)
    print(int(result))
