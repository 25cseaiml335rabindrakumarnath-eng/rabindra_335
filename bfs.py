from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


# User input
graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors separated by spaces: ").split()
    graph[node] = neighbors

start = input("Enter the starting node: ")

result = bfs(graph, start)

print("BFS Traversal:", result)
