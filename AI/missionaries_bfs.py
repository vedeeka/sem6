from collections import deque

def missionaries_cannibals_bfs(M, C, K):
    start = (M, C, 0)  # (Missionaries Left, Cannibals Left, Boat Side)
    goal = (0, 0, 1)

    Q = deque()
    Q.append((start, []))

    visited = set()
    visited.add(start)

    moves = []
    for m in range(K + 1):
        for c in range(K + 1):
            if 1 <= m + c <= K:
                moves.append((m, c))

    while Q:
        (ML, CL, B), path = Q.popleft()

        if (ML, CL, B) == goal:
            return path + [(ML, CL, B)]

        for m, c in moves:
            if B == 0:  # Boat on left → move to right
                ML_new = ML - m
                CL_new = CL - c
                B_new = 1
            else:       # Boat on right → move to left
                ML_new = ML + m
                CL_new = CL + c
                B_new = 0

            new_state = (ML_new, CL_new, B_new)

            # Check valid state
            if 0 <= ML_new <= M and 0 <= CL_new <= C:
                if ML_new == 0 or ML_new >= CL_new:
                    MR = M - ML_new
                    CR = C - CL_new
                    if MR == 0 or MR >= CR:
                        if new_state not in visited:
                            visited.add(new_state)
                            Q.append((new_state, path + [(ML, CL, B)]))

    return "No Solution"


# --- Input ---
M = int(input("Enter the number of Missionaries: "))
C = int(input("Enter the number of Cannibals: "))
K = int(input("Enter the Boat Capacity: "))

# --- Solve ---
solution = missionaries_cannibals_bfs(M, C, K)

# --- Output ---
if solution == "No Solution":
    print("\nNo Solution Found!")
else:
    print("\n===== Solution Steps =====\n")
    for i, (ML, CL, B) in enumerate(solution):
        MR = M - ML
        CR = C - CL
        side = "Left" if B == 0 else "Right"

        print(f"Step {i}:")
        print(f"  Left Bank  -> Missionaries: {ML}, Cannibals: {CL}")
        print(f"  Right Bank -> Missionaries: {MR}, Cannibals: {CR}")
        print(f"  Boat is on: {side}")
        print("-" * 40)