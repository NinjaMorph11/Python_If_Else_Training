# Break statements can break the loop containing it.

# Example 1

while True:
    print("Please type your name")
    name = input()
    if name == "your name":
        break
print("Thank you!")
