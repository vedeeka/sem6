import math


# Alpha-Beta Function
def alpha_beta(node, depth, alpha, beta, max_player, values):

    print("\nAlpha :", alpha,
          " Beta :", beta,
          " Depth :", depth)

    # Calculate maximum depth
    max_depth = int(math.log2(len(values)))

    # Leaf node condition
    if depth == max_depth:
        return values[node]

    # MAX Player
    if max_player:

        best = -math.inf

        for i in range(2):

            val = alpha_beta(
                node * 2 + i,
                depth + 1,
                alpha,
                beta,
                False,
                values
            )

            best = max(best, val)

            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                print("Pruned at depth", depth)
                break

        return best

    # MIN Player
    else:

        best = math.inf

        for i in range(2):

            val = alpha_beta(
                node * 2 + i,
                depth + 1,
                alpha,
                beta,
                True,
                values
            )

            best = min(best, val)

            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                print("Pruned at depth", depth)
                break

        return best


# ---------------- MAIN PROGRAM ---------------- #

# Number of leaf nodes
n = int(input("Enter number of leaf nodes: "))

# Check if number is power of 2
if (n & (n - 1)) != 0:
    print("Number of leaf nodes must be a power of 2")
    exit()

# Input leaf values
values = []

print("Enter leaf node values:")

for i in range(n):

    val = int(input(f"Value {i + 1}: "))

    values.append(val)

# Execute Alpha-Beta Pruning
result = alpha_beta(
    0,
    0,
    -math.inf,
    math.inf,
    True,
    values
)

# Final Result
print("\nOptimal Value :", result)