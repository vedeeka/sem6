import math

def hill_climbing(func, start, step_size=0.1, max_iterations=100):
    current_x = start
    current_value = func(current_x)

    # Print table header
    print(
        f"Start at x = {current_x:.4f}, "
        f"f(x) = {current_value:.4f}\n"
        f"{'Step':<6}{'Left':<32}{'Right':<32}{'Chosen'}"
    )
    print("-" * 95)

    for step in range(max_iterations):

        # Generate neighboring states
        left = current_x - step_size
        right = current_x + step_size

        # Evaluate neighbors
        left_value = func(left)
        right_value = func(right)

        chosen = "Current State"

        # Move to better neighbor
        if left_value > current_value:
            current_x = left
            current_value = left_value
            chosen = f"x = {left:.2f}"

        elif right_value > current_value:
            current_x = right
            current_value = right_value
            chosen = f"x = {right:.2f}"

        # Print step details
        print(
            f"{step + 1:<6}"
            f"{f'x = {left:.2f}, f(x) = {left_value:.2f}':<32}"
            f"{f'x = {right:.2f}, f(x) = {right_value:.2f}':<32}"
            f"{chosen}"
        )

        # Stop if no improvement
        if chosen == "Current State":
            print("\nNo better neighbors found. Algorithm converged.")
            break

    return current_x, current_value


# Allowed names for safe evaluation
allowed_names = {
    "x": 0,
    "math": math
}

# User input function
expression = input("Enter function in terms of x: ")

# Objective function
def objective_function(x):
    allowed_names["x"] = x
    return eval(expression, {"__builtins__": None}, allowed_names)


# Starting point
start_point = float(input("Enter starting x value: "))

# Step size
step = float(input("Enter step size: "))

# Run hill climbing
best_x, best_value = hill_climbing(
    objective_function,
    start=start_point,
    step_size=step
)

# Final result
print(f"\nBest x = {best_x:.4f}, f(x) = {best_value:.4f}")