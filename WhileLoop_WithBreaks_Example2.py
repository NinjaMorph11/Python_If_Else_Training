# Break statements can break the loop containing it.

# Example 2
k = 0
while k < 5:
    print(f'Outer For Loop Iteration: {k}')
    k += 1
    num = 0
    while num < 5:
        num += 1
        if num == 5:
            break  # Once num = 5, it exits the current loops. In this case, it went from inner loop to outer loop
        print(f'--Inner For Loop Iteration: {num}')
