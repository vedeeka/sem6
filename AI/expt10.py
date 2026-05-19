import heapq


# Function to display OPEN list
def display_open_list(open_list, g_cost):

    print(f"\n{'Node':<10}{'g':<10}{'h':<10}{'f':<10}")
    print("-" * 40)

    # Sort OPEN list for display
    temp = sorted(open_list)

    for f, node in temp:
        print(
            f"{node:<10}"
            f"{g_cost[node]:<10}"
            f"{heuristic[node]:<10}"
            f"{f:<10}"
        )


# A* Algorithm
def a_star(start, goal):

    # Priority queue for OPEN list
    open_list = []

    # Push start node with f = 0
    heapq.heappush(open_list, (0, start))

    # Initialize g costs
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    # Parent dictionary for path reconstruction
    parent = {start: None}

    # CLOSED list
    closed_list = set()

    while open_list:

        # Display OPEN list
        display_open_list(open_list, g_cost)

        # Pop node with smallest f value
        current_f, current = heapq.heappop(open_list)

        print(f"\nSelected Node: {current}")

        # Goal check
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, g_cost[goal]

        # Add current node to CLOSED list
        closed_list.add(current)

        # Explore neighbors
        for neighbor, cost in graph[current].items():

            if neighbor in closed_list:
                continue

            tentative_g = g_cost[current] + cost

            # Better path found
            if tentative_g < g_cost[neighbor]:

                parent[neighbor] = current
                g_cost[neighbor] = tentative_g

                f = tentative_g + heuristic[neighbor]

                heapq.heappush(open_list, (f, neighbor))

                print(
                    f"Updated: Node {neighbor}, "
                    f"g = {tentative_g}, "
                    f"h = {heuristic[neighbor]}, "
                    f"f = {f}"
                )

    return None, float('inf')


# ---------------- MAIN PROGRAM ---------------- #

graph = {}
heuristic = {}

# Number of vertices
n = int(input("Enter number of vertices: "))

# Input graph and heuristic values
for i in range(1, n + 1):

    graph[i] = {}

    num_neighbors = int(input(f"\nEnter number of neighbors of node {i}: "))

    for _ in range(num_neighbors):

        neighbor, cost = map(
            int,
            input("Enter neighbor and edge cost: ").split()
        )

        graph[i][neighbor] = cost

    h_val = int(input(f"Enter heuristic value of node {i}: "))

    heuristic[i] = h_val


# Start and goal nodes
start = int(input("\nEnter start node: "))
goal = int(input("Enter goal node: "))


# Run A* Algorithm
path, cost = a_star(start, goal)


# Output result
if path:
    print("\nOptimal Path:", path)
    print("Total Cost:", cost)
else:
    print("\nNo path found.")