# Break statements can break the loop containing it.

# Example 1
for num in range(0, 10):
    print(num)
    if num == 5:
        break
    print(f'Iteration: {num}')
