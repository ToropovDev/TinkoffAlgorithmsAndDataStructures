from collections import deque

n = int(input())
move_dict = {}
for _ in range(n):
    move_input = input().split(" -> ")
    from_node, to_node = move_input[0], move_input[1]
    if from_node not in move_dict:
        move_dict[from_node] = []
    move_dict[from_node].append(to_node)

start_node = input()
end_node = input()

len_dict = {}
queue = deque()
len_dict[start_node] = 0
queue.append(start_node)

while queue:
    current = queue.popleft()
    if current == end_node:
        print(len_dict[current])
        break
    if current in move_dict:
        for next_node in move_dict[current]:
            if next_node not in len_dict:
                len_dict[next_node] = len_dict[current] + 1
                queue.append(next_node)
else:
    print("-1")
