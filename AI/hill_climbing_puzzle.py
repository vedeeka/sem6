

def heuristic(state, goal):

    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                count += 1

    return count


def find_blank(state):

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def generate_neighbors(state):

    neighbors = []

    row, col = find_blank(state)


    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:


            new_state = [r[:] for r in state]

  
            new_state[row][col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[row][col]

            neighbors.append(new_state)

    return neighbors


def print_matrix(matrix):

    for row in matrix:
        print(row)


def hill_climbing(initial_state, goal_state):

    current = initial_state

    while True:

        print("\nCurrent State:")
        print_matrix(current)

        current_h = heuristic(current, goal_state)

        print("h(n) =", current_h)


        if current == goal_state:
            print("\nGoal Reached!")
            return current

        neighbors = generate_neighbors(current)

        best = None
        best_h = float('inf')

        print("\nNeighbors:\n")

        for neighbor in neighbors:

            h = heuristic(neighbor, goal_state)

            print_matrix(neighbor)
            print("h(n) =", h)
            print()

            if h < best_h:
                best_h = h
                best = neighbor


        if best_h >= current_h:
            print("No better neighbor found.")
            return current

        current = best




print("Enter Initial State Matrix (3x3):")

initial_state = []

for i in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

print("\nEnter Goal State Matrix (3x3):")

goal_state = []

for i in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)



result = hill_climbing(initial_state, goal_state)

print("\nFinal State:")

print_matrix(result)