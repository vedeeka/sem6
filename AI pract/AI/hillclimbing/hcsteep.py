def hill_climbing(graph, start, h):
    current = start
    path = [current]

    while True:
        best = None

        for neighbor in graph[current]:
            if h[neighbor] < h[current]:
                if best is None or h[neighbor] < h[best]:
                    best = neighbor

        if best is None:
            break

        current = best
        path.append(current)

    return path


graph = {}
h = {}

while True:
    node = input("Enter node (done to stop): ")
    if node.lower() == "done":
        break

    graph[node] = input(f"Enter neighbors of {node}: ").split()

print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"{node}: "))

start = input("\nEnter start node: ")

path = hill_climbing(graph, start, h)

print("\nPath:")
print(" -> ".join(path))






# def hill_climbing(graph,start,h):

#     current = start
#     path = [current]
#     while True:
#         move=False
#         best=current
#         for i in graph[current]:
#             if i not in path and  h[i]<h[best]:
#                     best=i
#                     move=True
#         current=best          

#         if not move:
#             break
#         path.append(current)
#     return path



# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['G'],
#     'F': [],
#     'G': []
# }

# h = {
#     'A': 10,
#     'B': 8,
#     'C': 6,
#     'D': 7,
#     'E': 5,
#     'F': 4,
#     'G': 0
# }

# start = 'A'

# print("Path:")
# print(" -> ".join(hill_climbing(graph, start, h)))