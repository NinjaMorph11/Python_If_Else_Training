# Break statements can break the loop containing it.

# Example 2
for k in range(0, 5):
    print(f'Outer For Loop Iteration: {k}')
    for num in range(0, 10):
        if num == 5:
            break  # Once num = 5, it exits the current loops. In this case, it went from inner loop to outer loop
        print(f'--Inner For Loop Iteration: {num}')
