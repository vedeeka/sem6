def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def dfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    stack = [(start, [start])]
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    solutions = []

    while stack:
        (m, c, b), path = stack.pop()

        if (m, c, b) == goal:
            solutions.append(path)
            continue

        for dm, dc in moves:
            if b == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            if valid(new[0], new[1]) and new not in path:
                stack.append((new, path + [new]))

    if solutions:
        for i, sol in enumerate(solutions, 1):
            print(f"\nSolution {i}:")
            for state in sol:
                print(state)
    else:
        print("No Solution")

dfs()