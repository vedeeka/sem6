from heapq import heappush, heappop

def best_first_search(graph, start, goal, h):
    pq = []
    visited = set()
    parent = {}

    heappush(pq, (h[start], start))
    parent[start] = None

    while pq:
        h_value, current = heappop(pq)

        if current == goal:
            break

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heappush(pq, (h[neighbor], neighbor))
                if neighbor not in parent:
                    parent[neighbor] = current

    if goal not in parent:
        return None

    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]

    return path[::-1]


graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    graph[node] = input(f"Neighbors of {node}: ").split()

print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"{node}: "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

path = best_first_search(graph, start, goal, h)

if path:
    print("Path:", " -> ".join(path))
else:
    print("No Path Found")














# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': ['H'],
#     'F': [],
#     'G': [],
#     'H': []
# }

# h = {
#     'A': 7,
#     'B': 6,
#     'C': 4,
#     'D': 5,
#     'E': 3,
#     'F': 2,
#     'G': 4,
#     'H': 0
# }

# start = 'A'
# goal = 'H'

# path = best_first_search(graph, start, goal, h)

# if path:
#     print("Path:", " -> ".join(path))
# else:
#     print("No Path Found")