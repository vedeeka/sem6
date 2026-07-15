def hill_climbing(graph, start, h):
    current = start
    path = [current]

    while True:
        next_node = None

        for neighbor in graph.get(current, []):
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