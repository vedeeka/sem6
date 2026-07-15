N = int(input("Enter the value of N: "))

cols = list(range(N))

def safe(k):
    for i in range(k):
        if abs(cols[i] - cols[k]) == abs(i - k):
            return False
    return True

def solve(k=0):
    if k == N:
        print_board()
        print("\n")
        return

    for i in range(k, N):
        cols[k], cols[i] = cols[i], cols[k]

        if safe(k) and solve(k + 1):
            return True

        cols[k], cols[i] = cols[i], cols[k]

    return False

def print_board():
    for r in range(N):
        for c in range(N):
            if cols[c] == r:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

if solve():
    print("\nSolution Found:\n")
    print_board()
else:
    print("No Solution Exists")