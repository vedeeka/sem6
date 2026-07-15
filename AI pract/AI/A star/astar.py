from heapq import heappush, heappop

def astar(graph, h, start, goal):
    pq = []
    parent = {}
    g = {}

    heappush(pq, (h[start], start))
    parent[start] = None
    g[start] = 0

    while pq:
        f, current = heappop(pq)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], g[goal]

        for neighbor, cost in graph.get(current, []):
            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = current
                heappush(pq, (new_g + h[neighbor], neighbor))

    return None, None


graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    m = int(input(f"Number of neighbors of {node}: "))

    graph[node] = []

    for _ in range(m):
        neighbor = input("Neighbor: ")
        cost = int(input("Cost: "))
        graph[node].append((neighbor, cost))

print("\nEnter heuristic values:")
for node in graph:
    h[node] = int(input(f"{node}: "))

start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

path, cost = astar(graph, h, start, goal)

if path:
    print("\nPath:", " -> ".join(path))
    print("Cost:", cost)
else:
    print("No Path Found")