def valid(m, c, tm, tc):
    if m < 0 or c < 0 or m > tm or c > tc:
        return False

    if m > 0 and m < c:
        return False

    nm = tm - m
    nc = tc - c

    if nm > 0 and nm < nc:
        return False

    return True


def dldfs(tm, tc, boat, limit):
    start = (tm, tc, 1)
    goal = (0, 0, 0)

    steps = []
    for i in range(boat + 1):
        for j in range(boat + 1):
            if 1 <= i + j <= boat:
                steps.append((i, j))

    stack = [(start, [start], 0)]

    while stack:
        (m, c, b), path, depth = stack.pop()

        if (m, c, b) == goal:
            print("Solution:")
            for s in path:
                print(s)
            return

        if depth >= limit:
            continue

        for i, j in reversed(steps):
            if b == 1:
                nm = m - i
                nc = c - j
                nb = 0
            else:
                nm = m + i
                nc = c + j
                nb = 1

            new_state = (nm, nc, nb)

            if valid(nm, nc, tm, tc) and new_state not in path:
                stack.append((new_state, path + [new_state], depth + 1))

    print("No Solution Within Depth Limit")


# Driver Code
m = int(input("Enter Missionaries: "))
c = int(input("Enter Cannibals: "))
boat = int(input("Enter Boat Capacity: "))
limit = int(input("Enter Depth Limit: "))

dldfs(m, c, boat, limit)