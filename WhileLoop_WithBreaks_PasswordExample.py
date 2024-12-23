# Break statements can break the loop containing it.

# Password Example
chance = 0
while chance < 5:
    chance += 1
    passwordchecker = input("Enter a password: ")
    if passwordchecker == ("python"):
        print("Password is correct")
        break
    print("please try again")

# In this example, break is to exit the loop. Entering the correct password will exit the password instead of going throught the loop
