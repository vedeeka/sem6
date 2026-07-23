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












def valid(m, c, tm, tc):
    if m < 0 or c < 0 or m > tm or c > tc:
        return False

    if m > 0 and c > m:
        return False

    rm = tm - m
    rc = tc - c
    if rm > 0 and rc > rm:
        return False

    return True


def dfs(tm, tc, boat):
    start = (tm, tc, 1)
    goal = (0, 0, 0)

    moves = []
    for i in range(boat + 1):
        for j in range(boat + 1):
            if 1 <= i + j <= boat:
                moves.append((i, j))

    stack = [(start, [start])]

    while stack:
        (m, c, b), path = stack.pop()

        if (m, c, b) == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        for dm, dc in moves:
            if b:
                new = (m - dm, c - dc, 0)
            else:
                new = (m + dm, c + dc, 1)

            if valid(new[0], new[1], tm, tc) and new not in path:
                stack.append((new, path + [new]))

    print("No Solution")


# Driver Code
m = int(input("Enter Missionaries: "))
c = int(input("Enter Cannibals: "))
boat = int(input("Enter Boat Capacity: "))

dfs(m, c, boat)