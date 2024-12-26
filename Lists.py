# List
this_list = ['cat', 'bat', 'rat']
print(this_list)

# I can have a list inside a list
this_listinsidealist = [["cat", "bat"], [10, 20, 30, 40]]
# This is known as getting the index of the list
print(this_listinsidealist[0][1])

# We can also use negative numbers in the index
print(this_listinsidealist[-1])

# Use slices : You can from index 0 to 1
print(this_listinsidealist[0:1])

# Index = Single Value
# Slice = List of Values

# Replace the items inside the list
this_listinsidealist[1] = "spam"
print(this_listinsidealist)

# Even with the usage of slices we can replace it
this_list[:2] = ["A bat", "A rat"]
print(this_list)

# We can also use other ways in slices to print the items inside a list
print(this_list[:2])  # This is technically 0:2

# Usage of del: Delete items inside a list
del this_list[2]
print(this_list)

# We can use len to count the items inside a list
print(len([1, 2, 3]))  # Output is 3

# Adding a list together
print([1, 2, 3] + [4, 5, 6])

# Multiplying a string
print("hello" * 3)

# Multiplying a list
print([1, 3, 4] * 3)

# The list() function : Converts the the object inside a list

# The in and not in Operators
"howdy" in ["hello", "hi", "howdy"]  # Returns True
"howdy" not in ["hello", "hi", "howdy"]  # Returns False
