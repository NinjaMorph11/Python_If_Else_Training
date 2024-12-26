# Methods

# index()
spam = ["Hye", 'Hello', 'Indeed']
print(spam.index("Hye"))  # Finding the index value of "Hye" inside the list

# Adding new values to list by append() and insert()
spam.append("Bye")  # Add at the end of the list
spam.insert(1, "Between")  # Adding new value at index 1

# Remove values with the remove() method
spam = ["Hye", 'Hello', 'Indeed']
spam.remove("Hye")
print(spam)

# sort()
# sort() can sort the list alphabetically and numerically
spam = [2, 3, 7, 9, 4, 2, 1]
spam.sort()
print(spam)
# I can even sort it in reverse
spam.sort(reverse=True)
print(spam)

# However, sort doesn't actually use alphabetical order, it uses ASCII-betical order
# Uppercase characters come first before lowercase characters
spam = ['Alice', 'Beta', 'alpha', 'bey']
spam.sort()
print(spam)
# Unless we add some key arguments
spam.sort(key=str.lower)
print(spam)
