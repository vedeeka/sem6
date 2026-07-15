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