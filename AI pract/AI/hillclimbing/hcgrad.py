def hill_climbing(graph, start, h):
    current = start
    path = [current]

    while True:
        next_node = None
        if current in graph:
            for neighbor in graph[current]:
                if h[neighbor] < h[current]:
                    next_node = neighbor
                    break

            if next_node is None:
                break

            current = next_node
            path.append(current)

    return path


graph = {}
h = {}

while True:
    node = input("Enter node (done to stop): ")
    if node.lower() == "done":
        break

    graph[node] = input(f"Neighbors of {node}: ").split()

print("\nEnter heuristic values")
for node in graph:
    h[node] = int(input(f"{node}: "))

start = input("\nStart node: ")

print("Path:")
print(" -> ".join(hill_climbing(graph, start, h)))


















# def hill_climbing(graph,start,h):

#     current = start
#     path = [current]
#     while True:
#         move=False

#         for i in graph[current]:
#             if i not in path and  h[i]<h[current]:
#                     path.append(i)
#                     current=i
#                     move=True
#                     break

#         if not move:
#             break

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