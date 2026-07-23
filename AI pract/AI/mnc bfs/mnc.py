from collections import deque

def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if (3-m) > 0 and (3-m) < (3-c):
        return False
    return True

def bfs():
    start = (3,3,1)
    goal = (0,0,0)

    queue = deque([(start,[start])])
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    solutions = []

    while queue:
        (m,c,b), path = queue.popleft()

        if (m,c,b) == goal:
            solutions.append(path)
            continue

        for dm, dc in moves:
            if b == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            # avoid cycles only in the current path
            if valid(new[0], new[1]) and new not in path:
                queue.append((new, path + [new]))

    if solutions:
        for i, sol in enumerate(solutions, 1):
            print(f"\nSolution {i}")
            for state in sol:
                print(state)
    else:
        print("No Solution")

bfs()















from collections import deque

def valid(m, c, tm, tc):
    if m < 0 or c < 0 or m > tm or c > tc:
        return False

    # Left bank
    if m > 0 and c > m:
        return False

    # Right bank
    rm = tm - m
    rc = tc - c
    if rm > 0 and rc > rm:
        return False

    return True


def bfs(tm, tc, boat):
    start = (tm, tc, 1)
    goal = (0, 0, 0)

    moves = []
    for i in range(boat + 1):
        for j in range(boat + 1):
            if 1 <= i + j <= boat:
                moves.append((i, j))

    q = deque([(start, [start])])

    while q:
        (m, c, b), path = q.popleft()

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
                q.append((new, path + [new]))

    print("No Solution")


# Driver
m = int(input("Enter Missionaries: "))
c = int(input("Enter Cannibals: "))
boat = int(input("Enter Boat Capacity: "))

bfs(m, c, boat)