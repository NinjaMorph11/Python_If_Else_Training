for i in [0, 1, 2, 3]:
    print(i)

# To get a list from a range
print(list(range(4)))

# range(len(list))
supplies = ["Pen", "Rubbers", "Pencils"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is " + supplies[i])

#  Multiple Assignment

cat = ["fat", "orange", "loud"]
size, color, diposition = cat
print(size)

# Another way of assignment
size, color, disposition = "skinny", 'black', 'quiet'

# Swapping variables
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print(b)

# Augmented Assignment Operators such as += 1
a += str(1)
print(a)
